
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v = torch.mm(x1, y1)  # Matrix multiplication of two input tensors
        v2 = torch.cat([v] * [5 for _ in range(len(v))])  # Concatenate the result tensor along a specified dimension
        
        return v2


# Initializing the model
m  = Model()
x1, y1 = torch.randn(30, 64), torch.randn(30)
 
# Input to the model
x1 = torch.randn(5, 30, 64).detach().requires_grad_()  # First input of the forward method must be a trainable tensor in order for autograd to work on it


# Initializing the loss function
loss = torch.nn.MSELoss()
 
# Computing the loss value with respect to the parameters and the gradients wrt. the tensors in the computational graph that was produced by calling the forward method of our model. The gradient will be added automatically during back propagation (backprop = compute_gradients + apply_gradients) 
loss(m(x1, y1), torch.randn(5)).backward()

