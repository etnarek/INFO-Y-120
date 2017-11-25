CC=tshark

CFLAGS=-T fields

CFLAGS+=-e dns.id 
CFLAGS+=-e ip.src 
CFLAGS+=-e ip.dst 
CFLAGS+=-e frame.time_epoch

CFLAGS+=-e dns.qry.type 
CFLAGS+=-e dns.qry.name.len 
CFLAGS+=-e dns.qry.name 
CFLAGS+=-e frame.len 
CFLAGS+=-e dns.resp.ttl 
CFLAGS+=-e dns.cname 
CFLAGS+=-e dns.a 
CFLAGS+=-e dns.aaaa
CFLAGS+=-e dns.txt

LDFLAGS=-E separator="/t" -E quote=d -E header=y

FILTER=-Y "dns.flags.response == 1"

%.csv:%.pcap
	time $(CC) $(CFLAGS) $(FILTER) $(LDFLAGS) -r $< | ./filter > $@
