

model_name = "model1"
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = x1.permute([0, 2, 1]) # Permute the input tensor A
        v2 = torch.bmm(v1, self.linear.weight, self.linear.bias).reshape(-1, 3) 
        return v2

model_weights = {'linear':torch.ones((3, 4))}
__output__=Model().forward(torch.randn([100, 2, 5]))
