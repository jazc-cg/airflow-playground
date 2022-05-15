from airflow.utils.decorators import apply_defaults
from airflow.operators.bash_operator import BashOperator


class MyBashOperator(BashOperator):

    template_fields = ('bash_command', 'command')


    @apply_defaults
    def __init__(
            self, 
            command,
            *args, **kwargs):

        super(MyBashOperator, self).__init__(bash_command=command, *args, **kwargs)
        self.command = command
