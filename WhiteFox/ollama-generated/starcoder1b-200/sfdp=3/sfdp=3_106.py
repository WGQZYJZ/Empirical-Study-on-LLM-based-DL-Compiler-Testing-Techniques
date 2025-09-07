
class Model(torch.nn.Module):
    def __init__(self, q_k=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale = torch.tensor([q_k], dtype=torch.float).to(device)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) * self.scale
        s = qk.softmax(dim=-1)
        d = torch.nn.functional.dropout(s, p=0.5)
        output = d.matmul(self.conv(x1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(4, 3, 64, 64).to(device)
x1 = m(input_tensor)
