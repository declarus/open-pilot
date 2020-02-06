from panda import Panda
panda = Panda()
panda.set_safety_mode(Panda.SAFETY_ELM327)
panda.can_clear(0)
print(panda.can_recv())

global kmsgs

while 1:
  kmsgs = panda.can_recv()
  nmsgs = []
  #print(kmsgs)
  for i in range(len(kmsgs)):
  	if kmsgs[i][0] == 1042:
  		print(kmsgs[i])
  kmsgs = nmsgs[-256:]
