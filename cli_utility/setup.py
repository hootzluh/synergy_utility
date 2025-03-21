# cli_utility/setup.py

import setuptools

setuptools.setup(
    name="synergy-cli-utility",
    version="0.1.0",
    description="Synergy Network CLI Utility",
    author="Your Name",
    packages=setuptools.find_packages(),
    install_requires=[
        # Your dependencies, e.g.:
        "argparse",
        "pqcrypto",
        "pycryptodome",
        "eth_account",
        "solana",
        "tronpy"
        # etc.
    ],
    entry_points={
        "console_scripts": [
            "synergy=cli_utility.synergy_cli_app:main"
        ]
    },
    python_requires=">=3.7",
)