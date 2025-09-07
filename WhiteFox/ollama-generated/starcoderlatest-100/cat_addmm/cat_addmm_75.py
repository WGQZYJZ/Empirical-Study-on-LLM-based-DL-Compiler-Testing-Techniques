
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.linear1 = torch.nn.Linear(320*159, 896)
        self.relu = torch.nn.ReLU()
        self.dropout = torch.nn.Dropout(p=0.4)
        self.linear2 = torch.nn.Linear(896, 128)
        self.batch_norm1 = torch.nn.BatchNorm2d(896)
        self.batch_norm2 = torch.nn.BatchNorm2d(128)
        self.linear3 = torch.nn.Linear(128, dim)
 
    def forward(self, x):
        x  = x.reshape(-1, 320*159).permute(0, 2, 1) # Transpose to NCHW 
        v1 = self.linear1(x)
        v2 = self.relu(v1)
        v2 = self.dropout(v2)
        v3 = self.linear2(v2)
        v4 = torch.nn.functional.batch_norm(self.batch_norm1(v3), self.batch_norm2, 0) 
        v5 = self.relu(v4)
        v6 = self.linear3(v5)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 896, 2*7+30, 1*3+5+1) # NCHW   (N: Batch size; C: Channel; H: Height; W: Width)
