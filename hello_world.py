from time import sleep

import luigi


class HelloTask(luigi.Task):
    def run(self):
        sleep(60)
        with open('hello.txt', 'w') as hello_file:
            hello_file.write('Hello')
            hello_file.close()


if __name__ == '__main__':
   luigi.run()
