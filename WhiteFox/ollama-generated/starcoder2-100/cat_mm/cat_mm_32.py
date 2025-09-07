class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2): 
        v1 = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        v2 = torch.cat([v1 for _ in [None] * 5], dim=0)  # Concatenation of the result tensor along a specified dimension
        return v2
        
m = Model()
        
__output__  = m(torch.randn(3, 4), torch.randn(4, 6))
    x1: Tensor of shape (3, 4) of type float32
    x2: Tensor of shape (4, 6) of type float32
    
x1 = torch.Tensor([[-0.8987525   , -1.598327     , -1.134846    ,  1.4739757 ]
  [ 1.5096372   , -0.753591      , -0.83051945  , -1.0349528 ]
  [-1.6066918   , -1.0547057    ,  0.542039     ,  0.09668573]])
x2 = torch.Tensor([[-0.5974198  , -1.1757847   , -1.4683933    , -0.45764735,  1.6935261 ]
  [-0.17878256 ,  1.1772784     , -1.3890294  ,  0.04000979  ,  0.3268697 ]
  [ 1.296506    , -0.30822438  , -1.1278697    , -0.7566494  ,  0.7858865 ]
  [-1.6427873  ,  0.9600503  ,  0.894494     , -0.3359427  ,  1.1763704 ]])
