
class Model(torch.nn.Module):
    def __init__(self, inp = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.mm(v1, inp) + inp
        return v2


# Initializing the model
m = Model()
inp = torch.randn(3, 64 * 64, requires_grad=True) # This is a tensor that will be passed as input to the matrix multiplication operation on `x1` and `x2`. It needs gradient.


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 64 * 64, requires_grad=True) # This is a tensor that will be passed as input to the matrix multiplication operation on `x1` and `x2`. It needs gradient.


# Forward pass of model with inputs x1 and x2
y = m(x1, x2)
print(m.conv.weight.requires_grad) # `weight` is a module parameter. You should always set requires_grad to true when you create a module parameter. If you don't do that then you will not be able to backpropagate the gradients of parameters created in this function. Hence, in order to use PyTorch autograd with your module, make sure that it has its own copy of any tensors used by this function.
print(m.conv.weight) # `weight` is a module parameter. The gradient will always be None as we do not calculate gradients for module parameters.


# Gradients with respect to input tensor x2
inp.requires_grad = True  # This is required as torch.mm calculates gradients of the second input only with respect to the first input. Therefore, in order for PyTorch autograd to compute gradient of `x1` you will have to manually calculate the gradients of `x2`.


y.backward(gradient=None, retain_graph=True)  # Setting retain_graph = True makes sure that we don't forget to set requires_grad=True again at the next point.
print(inp.grad) # This will be None as autograd cannot track this tensor for gradient calculation as it is neither input to the `m()` operation nor output from `y`.


# Gradients with respect to input tensor x1
m(x2).backward()  # Calling backward will calculate gradients of both the input parameters and their module weights. This should now be possible since PyTorch knows which tensors need to be tracked for gradient calculation. Hence, we can now call .grad attribute on `inp` and set requires_grad=True if we like.
print(m.conv.weight.grad) # This is a tensor that will be required as an input of the matrix multiplication operation in `forward()`. In order to track this gradient with respect to the weight of conv2d we need to manually calculate it before calling backward().



# Gradients with respect to the model parameters (i.e., gradients of weights and biases)
m(x1).backward()  # Calling backward will calculate gradients of both the input parameters and their module weights. This should now be possible since PyTorch knows which tensors need to be tracked for gradient calculation. Hence, we can now call .grad attribute on `inp` and set requires_grad=True if we like.


