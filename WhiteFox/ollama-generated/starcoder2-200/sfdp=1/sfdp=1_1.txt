

class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.Tensor([512]).to('cuda')
 
    def forward(self, q1, k1, v1):
        scale  = (q1.size(-1) ** -0.5).to('cuda').item() # Scale the dot product by the square root of the number of query features
        qk_1  = torch.nn.functional.scaled_dot_product(q1, k1 * self.scale) # Compute the dot product of a query and key tensor in fp32 mode
        return scaled_qk


# Initializing the model
m  = MyModel()


# Inputs to the model
q1  = torch.randn(4096, 512).to('cuda') # Create a query input in fp32 format
k1  = torch.randn(4096, 512).to('cuda').requires_grad_() # Create an example key tensor and also require gradients to be computed


# Initializing the optimizer
import torch.optim as optim
optimizer  = optim.Adam([{'params': [k1], 'lr': 0.1}])
 

# Training loop
for i in range(2):
    optimizer.zero_grad()
    v1  = m(q1, k1) # Compute a dot product of query and key tensors
    loss = torch.nn.functional.mse_loss(v1, v1) 
    loss.backward()
    optimizer.step()


# Finalizing the model
k2  = k1 - q1 * self._residual_value  # Remove the residual connection from the key tensor.


# Generating a sample input for the model using torch.manual_seed
torch.manual_seed(0)

