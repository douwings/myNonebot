# coding:utf-8
"""
@author:wing
@date: 2020/4/8
@summary:
    图片相似度定位
"""

import cv2

from use.test.qq.plugins.work import aircv


class ImgRecognize(object):
    def __init__(self, im_source, im_search=None):
        """
        :param im_source: 图片素材
        :param im_search: 需要查找的图片
        """
        self._im_source_im = cv2.imread(im_source)
        if im_search is not None:
            self._im_search_im = cv2.imread(im_search)

    def find_all_template(self, threshold: float = 0.5, maxcnt: int = 0, rgb: bool = False,
                          bgremove: bool = False) -> list:
        """
        定位 im_search 在 im_source 的位置
        :param threshold: 阈值，当相识度小于该阈值的时候，就忽略掉
        :param maxcnt: 查找到的最大个数
        :param rgb:
        :param bgremove: 自动移除背景，这个功能存在问题
        :return: 相似图片的位置和相似度信息
        """
        assert self._im_search_im is not None, "图片定位时 im_search 参数不能为空"
        res_seq = aircv.find_all_template(im_source=self._im_source_im, im_search=self._im_search_im,
                                          threshold=threshold, maxcnt=maxcnt, rgb=rgb, bgremove=bgremove)
        return res_seq

    def find_one_template(self, threshold: float = 0.95, maxcnt: int = 0, rgb: bool = False,
                          bgremove: bool = False) -> list:
        """获取相似度最大的图片信息"""
        res_seq = self.find_all_template(threshold=threshold, maxcnt=maxcnt, rgb=rgb,
                                         bgremove=bgremove)
        if res_seq:
            return res_seq[:1]
        return list()

    def mark_in_source(self, res_seq: list) -> None:
        """在 im_source 中标注查找的图片位置"""
        for pos_info in res_seq:
            rect = pos_info['rectangle']
            cv2.rectangle(self._im_source_im, rect[0], rect[3], color=(0, 0, 255), thickness= 10)
            print("图片定位信息: {}".format(pos_info))
        newimg = cv2.resize(self._im_source_im, (int(self._im_source_im.shape[1] / 3), int(self._im_source_im.shape[0] / 3)), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("图片定位", newimg)
        cv2.waitKey(0)

    def mark_in_pos(self, pos_1: tuple, pos_2: tuple) -> None:
        """
        在指定的矩形位置处绘制矩形
        :param pos_1: 矩形左上角坐标
        :param pos_2: 矩形右下角坐标
        :return:
        """
        cv2.rectangle(self._im_source_im, pos_1, pos_2, color=(0, 255, 0))
        cv2.imshow("图片定位", self._im_source_im)
        cv2.waitKey(0)

    def img_cut(self, x0: int, y0: int, x1: int, y1: int):
        """
        切 im_source 图 ，以图片左上角为 (x0,y0) 右下角为 (x1,y1)
        :param x0:
        :param y0:
        :param x1:
        :param y1:
        :return:
        """
        croped = self._im_source_im[y0:y1, x0:x1]
        cv2.imshow("crop img", croped)
        cv2.waitKey(0)


if __name__ == '__main__':
    source = r'D:\dingimg\1.png'
    search = r'D:\dingimg\clockOut.png'
    ir = ImgRecognize(im_source=source, im_search=search)
    rect = ir.find_one_template()
    print(rect)
    ir.mark_in_source(rect)
