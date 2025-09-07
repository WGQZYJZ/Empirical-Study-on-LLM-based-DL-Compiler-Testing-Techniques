
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def dropout(tensor, p=0.5): # Use a random number generator
        return torch.rand_like(tensor, ...).bernoulli_(p)

    @staticmethod
    def lowmem_dropout(tensor, p=0.5):  # Use a random number generator in order to avoid frequent memory allocations and copying
        if tensor.numel() > 1:
            return torch.nn.functional.dropout(tensor, p)

        value = torch.empty_like(tensor).bernoulli_(p)
        for idx in range(tensor.shape[0]):
            value[idx] = torch.rand_like(value[idx])
        if tensor.device != value.device:
            value = value.contiguous()
        return value


# Initializing the model with fallback_random=True
m = Model()
__output = m(...)  # Use the fallback method for running on a CPU device. The result should be a random number (with 100% probability of being `1.0`).
if __output == ...:
    return True

