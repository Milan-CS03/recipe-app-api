"""
test custom django management command
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psychop2Error
 
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """test commands"""

    def test_wait_for_db_ready(self, patched_check):
        "to check if db is ready or not"
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])

        