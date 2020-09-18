import os, subprocess

f = open('README.MD')
count = 0
intro = ''
while count < 7:
    intro += f.readline()
    count += 1

f.close()

f = open('sample.txt', 'w')
process = subprocess.Popen(['tree'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
stdout, stderr = process.communicate()
f.write(stdout.decode('utf-8'))
f.close()

op = open('README.MD', 'w')
f = open('sample.txt')
op.write(intro)
for line in f.readlines():
    if 'sample.txt' not in line:
        op.write(line + '<br>' + '\n')

op.close()
f.close()
os.remove('sample.txt')
