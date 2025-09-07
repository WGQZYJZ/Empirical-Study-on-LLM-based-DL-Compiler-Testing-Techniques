
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1, other=None): # Specify an argument for the second tensor to be added in the model.
        v2 = self.linear(x1) 
        if not other is None: 
            v3 = v2 + other
        else:
            v3 = v2
        return v3


# Initializing the model
m  = Model()


# Inputs to the model

* For the first call of "forward":  `x` is an array with shape `[1, 3]` that contains random values.
* For the second call: the second argument for the `other=` keyword should be a 5x4 array that contains random values.

* When calling "forward" twice, you are not allowed to use the `other` argument for the first call; in both cases only `v3 = v2` should be used.

* When calling "forward":  `x` is an array with shape `[1, 3]` that contains random values.
* For each call: the argument `other=None` must be provided.