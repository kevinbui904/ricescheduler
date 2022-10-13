##Author: Kevin Bui <buik@carleton.edu>
import pypandoc
import os
from arrow import get
from tempfile import NamedTemporaryFile
from ricescheduler import make_url, sorted_classes, schedule, output, date_formats, parse_registrar_table, fetch_registrar_table, locale
    
def main():
    year = 2019
    start_month = locale().month_number('january')
    start_day = 13
    last_month = locale().month_number('january')
    last_day = 30
    weekdays = ["Monday"]
    output_fmt = "html"
    semester = "Fall"
    try:
        start_date = [get(year, start_month, start_day)]
    except:
        return "The starting date you specified does not exist." 

    try:
        last_date = [get(year, last_month, last_day)]
    except:
        return "The ending date you specified does not exist." 

    possible_classes, no_classes = sorted_classes(weekdays, start_date, last_date, no_classes=[])
    course = schedule(possible_classes, no_classes, show_no=True, format=None)     

    suffix = '.' + output_fmt
    templatedir = os.path.dirname(os.path.abspath(__file__)) + '/templates'
    tf = NamedTemporaryFile(suffix=suffix)
    output(course, semester, str(year), output_fmt, templatedir=templatedir, outfile=tf.name)
    filename = semester + str(year) + 'Syllabus' + suffix


if __name__ == "__main__":
    main()