
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):  # A, B, C: the same shape (a, b)
        # Case 3: 1 input tensor is permuted and 2 other tensors are passed as the main argument.
        t1 = x1.permute([0] + [i for i in range(len(x1.shape)) if i not in {0}])
        t4 = torch.bmm(t1, y1)

        # Case 1: two input tensors are permuted and combined as the main argument.
        t2 = x1.permute([0] + [i for i in range(len(x1.shape)) if i not in {1}])
        t3 = torch.bmm(t2, y1)

        # Case 4: two input tensors are permuted and combined as the main argument.
        t5 = x1.permute([0] + [i for i in range(len(x1.shape)) if i not in {0}])
        t6 = torch.bmm(t2, y1)

        # Case 2: one input tensor is permuted and another is combined as the main argument.
        t7 = x1.permute([0] + [i for i in range(len(x1.shape)) if i not in {1}])
        t8 = torch.bmm(y1, t2)

        # Case 5: one input tensor is permuted and another is combined as the main argument.
        t9 = x1.permute([0] + [i for i in range(len(x1.shape)) if i not in {1}])
        t10 = torch.bmm(t7, y1)

        return t4+t3+t5+t6+t8+t9+t10


# Initializing the model