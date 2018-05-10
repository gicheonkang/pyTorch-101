import torch
from torch.autograd import Variable

batch_size = 100
row_lenth = 10
col_length = 10


def outer_product(x, y):
	return 0


if __name__ == '__main__':
	a = Variable(torch.randn((batch_size, row_lenth, col_length)))
	b = Variable(torch.randn((batch_size, row_lenth, col_length)))
	c = Variable(torch.randn((batch_size, row_lenth, col_length)))


	sum = Variable(torch.zeros((batch_size, row_lenth, col_length)))

	for i in range(batch_size):
		sum[i, :, :] = a[i, :, :] + b[i, :, :]

	d = torch.add(a, 1, b)
	e = torch.add(a, b)

	if torch.eq(d, e).sum() == 10000:
		print('true')
	else:
		print('false')
	
	#d = torch.eq(c, sum)
	

