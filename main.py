from pathlib import Path


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    out_dir = base_dir / "out"

    out_dir.mkdir(parents=True, exist_ok=True)

    # Implemente sua lógica aqui
    pass


if __name__ == "__main__":
    main()
