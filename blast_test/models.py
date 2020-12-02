from django.db import models


class BlastJob(models.Model):
    query = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.query


class BlastResult(models.Model):
    blast_job = models.ForeignKey(BlastJob, default=1, on_delete=models.CASCADE)
    result_no = models.IntegerField(blank=False, null=False)        # increase linearly i guess
    sstart = models.IntegerField(blank=False, null=False)           # no. 9
    send = models.IntegerField(blank=False, null=False)             # no. 10
    sstrand = models.CharField(max_length=5)                        # can be obtained
    evalue = models.FloatField(blank=False, null=False)             # no. 11
    pident = models.FloatField(blank=False, null=False)             # no. 3
    sequence = models.CharField(max_length=255, blank=False, null=False)  # probably sseq

    def __str__(self):
        return "%s %s" % (self.blast_job, self.result_no)
