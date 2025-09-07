
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def rand_like(*args):
        return torch.rand_like(*args)  # Replace the random function with the corresponding replacements
    
    @staticmethod
    def lowmem_dropout(*args, **kwargs):
        return torch.lowmem_dropout(*args, **kwargs)  # Replace the dropout function with the corresponding replacements
