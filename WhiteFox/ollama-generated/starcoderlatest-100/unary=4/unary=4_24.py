
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Test cases
## test_case_0:
  input:
  x1[N, C, H, W]: FloatTensor of shape (1, 3, 64, 64)
  
  output[N, O, H, W]: FloatTensor of shape (1, 8, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x2[B, C, N, H, W]: FloatTensor of shape (5, 3, 1, 64, 64)
  
  output[B, O, N, H, W]: FloatTensor of shape (5, 8, 1, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x3[N, C, N, H, W]: FloatTensor of shape (1, 3, 2, 64, 64)
  
  output[N, O, N, H, W]: FloatTensor of shape (1, 8, 2, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x4[B, C, B, H, W]: FloatTensor of shape (5, 3, 5, 64, 64)
  
  output[B, O, B, H, W]: FloatTensor of shape (5, 8, 5, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x5[N, C, N, H, W]: FloatTensor of shape (1, 3, 2, 64, 64)
  
  output[B, O, B, H, W]: FloatTensor of shape (1, 8, 5, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x6[N, C, N, H, W]: FloatTensor of shape (1, 3, 2, 64, 64)
  
  output[B, O, B, H, W]: FloatTensor of shape (1, 8, 5, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x7[N, C, N, H, W]: FloatTensor of shape (1, 3, 2, 64, 64)
  
  output[B, O, B, H, W]: FloatTensor of shape (1, 8, 5, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x8[N, C, N, H, W]: FloatTensor of shape (1, 3, 2, 64, 64)
  
  output[B, O, B, H, W]: FloatTensor of shape (1, 8, 5, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x9[N, C, N, H, W]: FloatTensor of shape (1, 3, 2, 64, 64)
  
  output[B, O, B, H, W]: FloatTensor of shape (1, 8, 5, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x10[N, C, N, H, W]: FloatTensor of shape (1, 3, 2, 64, 64)
  
  output[B, O, B, H, W]: FloatTensor of shape (1, 8, 5, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x11[N, C, N, H, W]: FloatTensor of shape (1, 3, 2, 64, 64)
  
  output[B, O, B, H, W]: FloatTensor of shape (1, 8, 5, 64, 64)
# generated test data ends here.


## test_case_0:
  input:
  x12[N, C, N, H,  0000000000000000000000000000000