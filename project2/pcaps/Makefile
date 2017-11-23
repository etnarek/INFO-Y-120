CC=tshark

CFLAGS=-T fields

CFLAGS+=-e dns.id 
CFLAGS+=-e dns.flags.response 
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

LDFLAGS=-E separator="," -E quote=d

%.csv:%.pcap
	time $(CC) $(CFLAGS) $(LDFLAGS) -r $< > $@
