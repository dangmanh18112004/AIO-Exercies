import torch
import torch.nn as nn

class Softmax(nn.Module):
	def __init__(self):
		super().__init__()

	def forward(self, x):
		tmp = torch.exp(x)
		return tmp / torch.sum(tmp)
	
class Softmax_stable(nn.Module):
	def __init__(self):
		super().__init__()

	def forward(self, x):
		c = max(x)
		tmp = torch.exp(x - c)
		return tmp / torch.sum(tmp)
	
# Test
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

softmax_stable = Softmax_stable()
output = softmax_stable(data)
print(output)
