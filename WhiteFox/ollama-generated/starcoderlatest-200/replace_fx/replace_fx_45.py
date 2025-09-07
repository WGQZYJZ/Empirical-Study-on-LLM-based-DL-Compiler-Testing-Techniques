
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # This line triggers the replacements above
        v2 = torch.rand_like(v1, v1) # This line will not trigger any replacement as we are running on a CPU device
        return v2


# Initializing the model and registering its input shape for pattern matching to be triggered during graph transformation.
m = Model()
model_signature = (torch.TensorType([None, 2], torch.float32),)
gm.register_shape_for_pattern(m, 'drop', model_signature)


# Initializing the random seed to ensure reproducibility.
torch.manual_seed(10)

# Inputs to the model
x = torch.randn(1, 2, 3)
