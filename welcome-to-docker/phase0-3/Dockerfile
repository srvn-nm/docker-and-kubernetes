FROM busybox:latest
RUN dd if=/dev/random of=/home/disk.img bs=1MB count=200
RUN rm /home/disk.img
