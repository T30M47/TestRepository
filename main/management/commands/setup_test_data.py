import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Proizvod_bezIndeksa, Proizvod_SIndeksom, Proizvod_KriviIndeks, Proizvod_DioIndeksa, Proizvod_bezIndeksa_MaloRedaka, Proizvod_SIndeksom_MaloRedaka, Proizvod_SIndeksom_VelikaKard, Proizvod_DioIndeksa_VelikaKard, Proizvod_KriviIndeks_VelikaKard
from main.factory import *

NUM_PROIZVODBEZINDEKSA = 100000
NUM_PROIZVODSINDEKSOM = 100000
NUM_PROIZVODDIOINDEKSA = 100000
NUM_PROIZVODKRIVIINDEKS = 100000
NUM_PROIZVODBEZINDEKSAMALOREDAKA = 100
NUM_PROIZVODSINDEKSOMMALOREDAKA = 100
NUM_PROIZVODSINDEKSOMVELIKAKARD = 100000
NUM_PROIZVODDIOINDEKSAVELIKAKARD = 100000
NUM_PROIZVODKRIVIINDEKSVELIKAKARD = 100000

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Proizvod_bezIndeksa, Proizvod_SIndeksom, Proizvod_KriviIndeks, Proizvod_DioIndeksa, Proizvod_bezIndeksa_MaloRedaka, Proizvod_SIndeksom_MaloRedaka, Proizvod_SIndeksom_VelikaKard, Proizvod_DioIndeksa_VelikaKard, Proizvod_KriviIndeks_VelikaKard]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PROIZVODBEZINDEKSA):
            proizvod_bezIndeksa_inst = Proizvod_BezIndeksaFactory()

        for _ in range(NUM_PROIZVODSINDEKSOM):
            proizvod_sIndeksom_inst = Proizvod_SIndeksomFactory()

        for _ in range(NUM_PROIZVODDIOINDEKSA):
            proizvod_DioIndeksa_inst = Proizvod_DioIndeksaFactory()

        for _ in range(NUM_PROIZVODKRIVIINDEKS):
            proizvod_KriviIndeks_inst = Proizvod_KriviIndeksFactory()

        for _ in range(NUM_PROIZVODBEZINDEKSAMALOREDAKA):
            Proizvod_bezIndeksa_MaloRedaka_inst = Proizvod_BezIndeksa_MaloRedaka_Factory()

        for _ in range(NUM_PROIZVODSINDEKSOMMALOREDAKA):
            Proizvod_SIndeksom_MaloRedaka_inst = Proizvod_SIndeksom_MaloRedaka_Factory()

        for _ in range(NUM_PROIZVODKRIVIINDEKSVELIKAKARD):
            Proizvod_SIndeksom_VelikaKard_inst = Proizvod_SIndeksom_VelikaKard_Factory()

        for _ in range(NUM_PROIZVODDIOINDEKSAVELIKAKARD):
            Proizvod_DioIndeksa_VelikaKard_inst = Proizvod_DioIndeksa_VelikaKard_Factory()

        for _ in range(NUM_PROIZVODKRIVIINDEKSVELIKAKARD):
            Proizvod_KriviIndeks_VelikaKard_inst = Proizvod_KriviIndeks_VelikaKard_Factory()