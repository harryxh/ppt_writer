"""Tests for generator module."""

import pytest
from src.generator.ppt_generator import PPTGenerator, TEMPLATES


def test_generator_init():
    """Test PPTGenerator initialization."""
    generator = PPTGenerator()
    assert generator.template == "default"


def test_generator_init_with_template():
    """Test PPTGenerator with custom template."""
    generator = PPTGenerator(template="modern")
    assert generator.template == "modern"


def test_generator_invalid_template():
    """Test PPTGenerator with invalid template."""
    with pytest.raises(ValueError):
        PPTGenerator(template="invalid")
