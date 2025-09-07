
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    @staticmethod
    def is_valid_splitwithsizes_cat(model, input_tensor, split_sizes, concatenated_dim):
        if len(split_sizes) == 1:
            return True
        
        for i in range(len(split_sizes)):
            dim = i + 1  # The dim of the current tensor to be used is 1-based
            
            if model.conv[dim](input_tensor).shape != split_sizes[i]:
                return False
            
            if torch.all(model.conv[dim](input_tensor) == torch.zeros(split_sizes[i], *input_tensor.shape[2:])):
                return False
        
        if concatenated_dim is not None and model.conv[concatenated_dim](concatenated_tensor).shape != split_sizes[-1]:
            return False
        
        return True


# Initializing the model
m = Model()


