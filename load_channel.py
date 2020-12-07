import numpy as np
import scipy.io as sci


def load_channel_mat(H_folder_train_path, train_idx_low, train_idx_high):
    channel_response_set_train = []
    txt_line = 0
    for train_idx in range(train_idx_low, train_idx_high):
        H_file = H_folder_train_path + str(train_idx) + '.mat'
        data = sci.loadmat(H_file)
        h = np.array(list(data['box']))
        txt_line = 0
        for line in range(len(h)):
            numbers_str = h[line]
            numbers_float = [float(x) for x in numbers_str]
            h_response = np.asarray(numbers_float[0:int(len(numbers_float) / 2)]) + 1j * np.asarray(numbers_float[int(len(numbers_float) / 2):len(numbers_float)])
            # h_response = np.asarray(numbers_float[0:120]) + 1j * np.asarray(numbers_float[300:420])
            channel_response_set_train.append(h_response[0:120])
            txt_line += 1
    return channel_response_set_train, txt_line


if __name__ == '__main__':
    channel_response_set, h_line = load_channel_mat('F:\\channel\\NCS\\NCS', 1, 61)
