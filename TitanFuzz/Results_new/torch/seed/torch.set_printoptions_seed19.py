input_data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
input_tensor = torch.from_numpy(input_data)
torch.set_printoptions(precision=4, threshold=2, edgeitems=2, linewidth=80, profile=None, sci_mode=None)