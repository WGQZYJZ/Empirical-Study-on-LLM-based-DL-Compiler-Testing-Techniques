
class Model(torch.nn.Module):
    def __init__(self, size=None):
        super().__init__()

    def forward(self, input_tensors):
        t1 = torch.cat(input_tensors, dim=1)  # Concatenate the tensors in the list along dimension 1
        if (size is None or len(t1.shape) == 0):
            raise RuntimeError('Cannot slice tensor, as the number of elements to be sliced from the concatenation is not provided.')
        t2 = t1[:, :int(len(input_tensors))] # Slice the concatenated tensor along dimension 1
        if (size != None and size < len(t1.shape)):
            raise RuntimeError('Invalid slicing index: Size (%s) must be equal to or less than the number of elements in input tensors (%d)' % (size, len(input_tensors)))
        
        t3 = t2[:, :int(size)] # Slice the concatenated tensor along dimension 1
        t4 = torch.cat([t1, t3], dim=1) # Concatenate the concatenated tensor and sliced concatenation along dimension 1
        return t4

# Initializing the model
size = None
m = Model(size=None)

