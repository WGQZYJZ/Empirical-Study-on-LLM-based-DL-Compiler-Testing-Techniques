
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return self.linear(x1)
    
    @staticmethod
    def lowmem_dropout(input_tensor, p=0.5):  # Pseudo-random dropout to simulate the behavior of dropout_layer and replace_fx when not enough RAM is available for the model
        assert p in [0., 1.], "invalid dropout probability."

        # Perform dropout
        x = input_tensor if random() < p else torch.zeros_like(input_tensor)
        
        return x

    @staticmethod
    def rand_like(x):  # Generate a tensor with the same size as `x` filled with random numbers
        x_like = torch.ones_like(x, requires_grad=False)
        x_like.copy_(x)
        return x_like

# Initializing the model
m = Model()
__input__  = m(x1)
m.lowmem_dropout(__input__)

