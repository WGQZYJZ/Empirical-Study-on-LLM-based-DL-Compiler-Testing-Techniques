
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5)  # Apply dropout to the input tensor
        v2 = torch.rand_like(v1)  # Generate a random tensor of the same size as v1 with random numbers
        return (v1 + v2).tanh()


# Initializing the model and setting the replacements in `torch.backends.cuda` module.
m  = Model().to("cpu")
torch.backends.cuda._C.fallback_random = False # The fallback mode is disabled by default in `torch.backends.cuda` module, which prevents this example to run successfully with a single GPU device or without setting a config of CUDA_VISIBLE_DEVICES=0
m2  = Model().to("cpu")

