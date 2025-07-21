import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], [9.779], [6.182], [7.59], [2.167], [7.042], [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)
input_data = torch.from_numpy(input_data)
linear_model = torch.nn.Linear(1, 1)