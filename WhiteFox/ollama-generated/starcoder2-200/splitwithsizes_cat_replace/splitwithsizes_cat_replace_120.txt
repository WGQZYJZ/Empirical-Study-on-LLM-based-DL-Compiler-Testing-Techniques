
import torch
class Model(torch.nn.Module):
    def __init__(self, shape1=20000, shape2=(48,), shape3=750000, shape4=(6977419,), batchsize=2, device='cuda'):
        super().__init__()
        self.shape = torch.tensor([*shape2] + [batchsize], device=device)
        self.split_sizes = list(self._get_valid_splitwithsizes(len(self.shape)))
        self.conv1d  = torch.nn.Conv1d(3, 800, 945677, 2, 0).to(device)
        self.maxpool1d  = torch.nn.MaxPool1d(kernel_size=self._get_valid_splitwithsizes(len(shape4)),
                                              stride=torch.tensor([batchsize] + [1]*(3 if batchsize > 1 else 2)),
                                              padding=[0, *[(i-1)//2 for i in shape4]]).to(device)
        self.maxpool1d_1 = torch.nn.MaxPool1d(kernel_size=shape4[-1]//batchsize+[5],
                                               stride=[3 if batchsize > 1 else 0]*len(self.shape),
                                               padding=torch.tensor([*[(i-1)//2 for i in shape4]])).to(device)
        self.flatten = torch.nn.Flatten().to(device)
        self.relu = torch.nn.ReLU()
        self.linear_0  = torch.nn.Linear(80, 3).to(device)
 
    def forward(self, *args):
        t1 = self._split(t1)
        t2 = self.conv1d(t1)
        t4 = self.maxpool1d_1(torch.roll(torch.cat([tensor for tensor in t3], -1), 1))
        t5 = torch.relu(self.linear_0(self.flatten(t6)))
        return t7, t8
 
    def _get_valid_splitwithsizes(self, len):
        return [len//2] * ((4//(-1*len+3)) * (-1*len+3) // 5 + 1)
 
    def _split(self, input_tensor):
       return torch.split(input_tensor, self._get_valid_splitwithsizes(*self.shape), dim=0)

# Initializing the model:
model = Model(shape2=(48,), device='cuda')
model = model.to('cpu').eval()
__output__, __return1__, __return2__  = model(torch.zeros([75000, 3])) # Returns (3, 6977) tuple of tensors
assert torch.all(torch.isnan(__output__)) is False

