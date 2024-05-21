# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"22532.0","system":"readv2"},{"code":"98424.0","system":"readv2"},{"code":"37329.0","system":"readv2"},{"code":"16194.0","system":"readv2"},{"code":"97455.0","system":"readv2"},{"code":"36804.0","system":"readv2"},{"code":"39882.0","system":"readv2"},{"code":"34170.0","system":"readv2"},{"code":"55312.0","system":"readv2"},{"code":"98959.0","system":"readv2"},{"code":"96303.0","system":"readv2"},{"code":"58738.0","system":"readv2"},{"code":"50581.0","system":"readv2"},{"code":"67906.0","system":"readv2"},{"code":"32239.0","system":"readv2"},{"code":"58055.0","system":"readv2"},{"code":"99779.0","system":"readv2"},{"code":"16629.0","system":"readv2"},{"code":"66369.0","system":"readv2"},{"code":"39964.0","system":"readv2"},{"code":"45908.0","system":"readv2"},{"code":"94848.0","system":"readv2"},{"code":"10999.0","system":"readv2"},{"code":"4785.0","system":"readv2"},{"code":"55978.0","system":"readv2"},{"code":"72903.0","system":"readv2"},{"code":"16264.0","system":"readv2"},{"code":"53869.0","system":"readv2"},{"code":"43496.0","system":"readv2"},{"code":"31684.0","system":"readv2"},{"code":"31619.0","system":"readv2"},{"code":"27424.0","system":"readv2"},{"code":"21685.0","system":"readv2"},{"code":"65993.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('posterior-uveitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["posterior---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["posterior---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["posterior---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
