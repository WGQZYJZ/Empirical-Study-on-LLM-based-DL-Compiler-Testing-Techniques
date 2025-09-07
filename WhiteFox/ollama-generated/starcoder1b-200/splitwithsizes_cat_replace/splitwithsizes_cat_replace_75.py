
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def split_tensor(input_tensor, sizes):
        return input_tensor[i] for i in range(len(sizes))
 
    def concat(input_tensor, sizes):
        output = []
        split_tensors = [Model.split_tensor(input_tensor, sizes)
                         for _ in range(len(sizes))]

        # If only one tensor is concatenated and it contains no split_tensor,
        # return an empty list as well as True to avoid any further optimization
        if len(split_tensors) == 1:
            return output + [], True
 
        for s in split_tensors:
            output.append(s)

        return output


# Initializing the model
m = Model()
__output__, __success__ = m.is_valid_splitwithsizes_cat([[0], [1, 2]])


