from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = nn.Linear(2, 3)
        self.linear2  = nn.Linear(3, 4)

    def forward(self, x):
        v1  = torch.nn.functional.dropout(x, p=0.5, training=True) # apply dropout
        v2  = torch.nn.functional.relu(v1) # linear relu
        v3  = torch.nn.functional.softmax(self.linear1(v2)) # apply linear on result of previous function call to re-order tensor
        v4  = self.linear2(v3, True) # pass 'inplace' argument
        return v4
