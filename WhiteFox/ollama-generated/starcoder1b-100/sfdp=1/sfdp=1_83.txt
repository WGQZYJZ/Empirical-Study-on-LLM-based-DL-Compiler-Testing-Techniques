
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.fc   = torch.nn.Linear(in_features=5760, out_features=3, bias=True)
 
    def forward(self, x):
        v  = self.conv(x)  # Compute the input tensor of the convolution
        q = self.fc(v).squeeze(-1)   # Project the output of the first hidden layer to the output dimensionality
        k = torch.zeros_like(q).scatter_(0, q.argmax(-1, keepdim=True), 1)
        v = v + 1  # Add a bias to the input tensor of the convolution
        