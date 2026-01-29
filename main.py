"""Main entry point for PPT Writer."""

import argparse
import logging
from pathlib import Path

from src.scraper.web_scraper import WebScraper
from src.generator.ppt_generator import PPTGenerator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="AI PPT Generator")
    parser.add_argument("--topic", type=str, required=True, help="Presentation topic")
    parser.add_argument("--slides", type=int, default=10, help="Number of slides")
    parser.add_argument("--output", type=str, default="output.pptx", help="Output filename")
    parser.add_argument("--template", type=str, default="default", help="Template name")
    parser.add_argument("--web-search", action="store_true", help="Enable web search")
    
    args = parser.parse_args()
    
    logger.info(f"Generating PPT for: {args.topic}")
    
    # Initialize components
    scraper = WebScraper(enable_search=args.web_search)
    generator = PPTGenerator(template=args.template)
    
    # Collect content
    logger.info("Collecting content...")
    content = scraper.collect(topic=args.topic, max_results=args.slides)
    
    # Generate presentation
    logger.info("Generating presentation...")
    output_path = generator.create(
        content=content,
        topic=args.topic,
        num_slides=args.slides,
        output_file=args.output
    )
    
    logger.info(f"Presentation saved to: {output_path}")


if __name__ == "__main__":
    main()
