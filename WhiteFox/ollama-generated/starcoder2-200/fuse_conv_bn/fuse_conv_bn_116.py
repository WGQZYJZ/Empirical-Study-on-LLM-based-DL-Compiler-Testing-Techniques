

model = torch.nn.Sequential(
    torch.nn.Linear(4, 3), # linear layer with 4 input features and 3 output features 
    torch.nn.ReLU(), # non-linear ReLU function 
    torch.nn.Linear(20, 5)  # second linear layer
)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return self._f1()

    @torch.jit.script
    def _f1(): 
        t = torch.randn(32)  # dummy tensor, not in the model 
        a = torch.relu(t)    # non-linear ReLU function 
        b = torch.matmul(a, 400 * 3).sigmoid()  # 3 times 3 matrix multiplication
        return (b)

    def forward_with_return_(self):
      return self._f1()

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return self._f1(x) 

    @torch.jit.script
    def _f1(): 
        t = torch.randn(32)  # dummy tensor, not in the model 
        a = torch.relu(t)    # non-linear ReLU function 
        b = torch.matmul(a, 400 * 3).sigmoid()  # 3 times 3 matrix multiplication
        return (b)

    def forward_with_return_(self):
      return self._f1()

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return self._f1(x) 

    @torch.jit.script 
    def _f1(): 
        t = torch.randn(32)  # dummy tensor, not in the model 
        a = torch.relu(t)    # non-linear ReLU function 
        b = torch.matmul(a, 400 * 3).sigmoid()  # 3 times 3 matrix multiplication
        return (b)

    def forward_with_return_(self):
      return self._f1()

m = Model()

# Input to the model
x1 = torch.randn(20, 4)

