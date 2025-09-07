import argparse
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import run_pipeline

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=True, help="Input file path")
    parser.add_argument("-o", "--output", default="Outputs/", help="Output directory")
    parser.add_argument("-f", "--fill", default="N/A", help="Strategy for filling missing values")
    parser.add_argument("-s", "--summary", action='store_true')

    args = parser.parse_args()

    clean_df, report = run_pipeline(args.input, args.output, args.fill)
    print("Cleaned data:\n", clean_df)
    if args.summary:
        print("Summary:\n", report)

if __name__ == "__main__":
    main()