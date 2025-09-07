
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # conv(x1)
        v2  = torch.sigmoid(v1) # sigmoid(v1)
        v3  = v1 * v2  # v1*v2
        return v3


# Initializing the model and assigning random values to the weights of the layers in the model, and then printing out the initial weight values of all parameters.
m  = Model()

for name, param in m.named_parameters():
    if 'weight' not in name:
        continue
    print(name, param)


[('conv.weight', Parameter containing: 
 -1.9336 -0.8327  0.5478  ..., 1.7526 -0.4630 -0.7766])]

# Assigning the initial values to the weights of all layers in the model. 
for name, param in m.named_parameters():
    if 'weight' not in name:
        continue 
    param = torch.tensor([[1.,  2.],
 [3.,  4.],
  [5.,  6.],
  [7.,  8.],], requires_grad=True)

print(param)

 tensor([[ 1.,  2.],
[ 3.,  4.],
[ 5.,  6.],
[ 7.,  8.]], requires_grad=True)


