from __future__ import print_function
import os

from IPython.qt.console.rich_ipython_widget import RichIPythonWidget
from IPython.qt.inprocess import QtInProcessKernelManager
from IPython.lib import guisupport


def print_process_id():
    print('Process ID is:', os.getpid())


def main(**variables):
    # Print the ID of the main process
    print_process_id()

    app = guisupport.get_app_qt4()

    # Create an in-process kernel
    # >>> print_process_id()
    # will print the same process ID as the main process
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    kernel = kernel_manager.kernel
    kernel.gui = 'qt4'
    kernel.shell.push(variables)

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    def stop():
        kernel_client.stop_channels()
        kernel_manager.shutdown_kernel()
        app.exit()

    control = RichIPythonWidget()
    control.kernel_manager = kernel_manager
    control.kernel_client = kernel_client
    control.exit_requested.connect(stop)
    control.show()


if __name__ == '__main__':
    main()
