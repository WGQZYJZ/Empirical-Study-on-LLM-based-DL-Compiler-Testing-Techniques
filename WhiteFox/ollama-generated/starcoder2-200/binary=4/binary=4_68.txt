
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(200 * 5376 + 512, 4)
 
    def forward(self, x): 
        v0 = self._inner(x)[0] # Applying a linear transformation to the input tensor
 
        v1 = torch.add(v0, torch.tensor([5., -8.], dtype=torch.float32))
        return v1
 
m  = Model() 
 
inputs_to_model  = {
    'x': 
    torch.randn(64 * 5, 10) # random input to the linear transformation layer
}
outputs = m(**inputs_to_model)

