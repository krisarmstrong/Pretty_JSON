import json
import sys

def main():
    
    if len(sys.argv) < 3:
        print("Usage: py_json_pretty.py <inputfile.json>, <outputfile.json>")
        sys.exit()

    input_json_file = sys.argv[1]
    output_json_file = sys.argv[2]
    
    with open(input_json_file, 'r') as json_file:
        json_object = json.load(json_file)

    print(json_object)

    print(json.dumps(json_object))

    print(json.dumps(json_object, indent=1))

    json_object_output = (json.dumps(json_object, indent=1))

    with open(output_json_file,'w') as out_json_file:
        out_json_file.write(json_object_output)

if __name__ == "__main__":
    main()