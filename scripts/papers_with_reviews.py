from openreview_visualization.data.fetcher import OpenReviewFetcher
from openreview_visualization.data.processor import OpenReviewProcessor
from openreview_visualization.utils import save_json
import os
from openreview_visualization.data.fetcher import OpenReviewFetcher
from openreview_visualization.utils import save_jsonl
import pandas as pd
import orjson

if __name__ == "__main__":
    conference = "ICLR"
    year = 2024
    paper_csv_file = f"data/processed/{conference}{year}/paperlist.csv"
    raw_review_file = f"data/raw/{conference}{year}/raw_paper_reviews.jsonl"
    paper_with_review_file = f"data/processed/{conference}{year}/paper_with_review.csv"
    
    fetcher = OpenReviewFetcher(conference, year, batch_limit=10, limit=10)
    papers, count = fetcher.fetch_papers()
    # save_json({"notes": papers, "count": count}, "data/raw/iclr2025/raw_paperlist.json")
    print(papers)
    
    processor = OpenReviewProcessor()
    paper_df = processor.process_papers(papers)
    paper_df.to_csv(paper_csv_file, index=False)

    # papers = pd.read_csv(paper_csv_file)
    # fetcher = OpenReviewFetcher(conference, year)
    # reviews = fetcher.fetch_reviews(papers["id"].tolist())
    # save_jsonl(reviews, raw_review_file)
    
    # processor = OpenReviewProcessor()

    # with open(raw_review_file, "r") as f:
    #     reviews = [orjson.loads(line) for line in f]

    # review_df = processor.process_reviews(reviews)
    # review_df.sort_values(by=["avg_rating", "std_dev"], ascending=[False, True], inplace=True)
    # review_df.to_csv(paper_with_review_file, index=False)
    
    #     # Merge paper and review data
    # merged_df = pd.merge(paper_df, review_df, on="id", how="inner")
    # merged_df.sort_values(by=["avg_rating", "std_dev"], ascending=[False, True], inplace=True)

    # # Save final data to CSV
    # merged_df.to_csv(paper_with_review_file, index=False)
