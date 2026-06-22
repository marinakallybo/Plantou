import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from recomendador.models import Cultura


class Command(BaseCommand):
    help = "Importa culturas a partir de um arquivo CSV."

    def handle(self, *args, **options):
        caminho_csv = Path("data/culturas.csv")

        if not caminho_csv.exists():
            self.stdout.write(
                self.style.ERROR("Arquivo data/culturas.csv não encontrado.")
            )
            return

        with open(caminho_csv, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            culturas_criadas = 0
            culturas_atualizadas = 0

            for linha in leitor:
                cultura, criada = Cultura.objects.update_or_create(
                    nome=linha["nome"],
                    defaults={
                        "descricao": linha["descricao"],
                        "temperatura_minima": float(linha["temperatura_minima"]),
                        "temperatura_maxima": float(linha["temperatura_maxima"]),
                        "solo_ideal": linha["solo_ideal"],
                        "umidade_ideal": linha["umidade_ideal"],
                        "epoca_plantio": linha["epoca_plantio"],
                        "tempo_colheita_dias": int(linha["tempo_colheita_dias"]),
                        "dificuldade": linha["dificuldade"],
                    },
                )

                if criada:
                    culturas_criadas += 1
                else:
                    culturas_atualizadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Importação finalizada! "
                f"{culturas_criadas} culturas criadas e "
                f"{culturas_atualizadas} atualizadas."
            )
        )