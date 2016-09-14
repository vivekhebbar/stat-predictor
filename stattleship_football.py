from stattlepy import Stattleship


accessToken = "d49525fb16260a10a902f32b33aaa172"

def getAllPositions():
	New_query = Stattleship()
	Token = New_query.set_token(accessToken)
	qb_list = []
	rb_list = []
	wr_list = []
	te_list = []
	for i in range(250):
		Output = New_query.ss_get_results(sport='football',league='nfl',ep='players',page=str(i))
		qbs = filter(lambda row: row['position_name']=='Quarterback', Output[0]['players'])
		rbs = filter(lambda row: row['position_name']=='Running Back', Output[0]['players'])
		wrs = filter(lambda row: row['position_name']=='Wide Receiver', Output[0]['players'])
		tes = filter(lambda row: row['position_name']=='Tight End', Output[0]['players'])
		qb_names = map(lambda row: row['name'], qbs)
		rb_names = map(lambda row: row['name'], rbs)
		wr_names = map(lambda row: row['name'], wrs)
		te_names = map(lambda row: row['name'], tes)
		qb_list += qb_names
		rb_list += rb_names
		wr_list += wr_names
		te_list += te_names
	print(rb_list)
	print(wr_list)
	print(te_list)
	return qb_list, rb_list, wr_list, te_list

def getAllPlayers(position_name):
	New_query = Stattleship()
	pos_list = []
	Token = New_query.set_token(accessToken)
	for i in range(220):
		Output = New_query.ss_get_results(sport='football',league='nfl',ep='players',page=str(i))
		pos = filter(lambda row: row['position_name']==position_name, Output[0]['players'])
		pos_names = map(lambda row: row['name'], qbs)
		pos_list += pos_names
	print(pos_list)
	return pos_list


def computePoints(query, player_id):
	return None


qb_list, rb_list, wr_list, te_list = getAllPositions()

with open('qb_list.text','w') as f:
	for qb in qb_list:
		f.write(qb + "\n")
with open('rb_list.txt', 'w') as f:
	for rb in rb_list:
		f.write(rb + "\n")
with open('wr_list.txt', 'w') as f:
	for wr in wr_list:
		f.write(wr + "\n")
with open('te_list.txt', 'w') as f:
	for te in te_list:
		f.write(te + "\n")

