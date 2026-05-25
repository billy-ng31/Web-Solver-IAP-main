import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip } from 'recharts';

// 1. Khai báo nhận thêm dữ liệu assignments để làm "cò súng" kích hoạt cập nhật
export function BenchmarkDashboard({ assignments }: { assignments?: any }) {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    // 2. Thêm đuôi "?t=..." để ép trình duyệt không bao giờ lưu cache file này
    const timestamp = new Date().getTime();
    
    fetch(`/benchmark_result.json?t=${timestamp}`)
      .then(res => {
         if (!res.ok) throw new Error("Chưa tìm thấy file JSON");
         return res.json();
      })
      .then(json => setData(json))
      .catch(err => console.error("Lỗi lấy dữ liệu Benchmark:", err));
      
  }, [assignments]); // 3. Rất quan trọng: Báo cho React biết phải chạy lại fetch mỗi khi assignments thay đổi

  if (!data) return <div className="p-4 mt-8 font-semibold text-blue-600 animate-pulse">Đang nạp dữ liệu đánh giá Benchmark...</div>;


  return (
    <div className="p-4 bg-white rounded shadow mt-4">
      <h2 className="text-xl font-bold text-red-600 mb-4">
        Tổng điểm phạt: {data.total_score}
      </h2>
      
      {/* 1. Vẽ biểu đồ */}
      <div className="mb-8">
        <h3 className="font-semibold mb-2">Biểu đồ Ràng buộc mềm</h3>
        <BarChart width={600} height={300} data={data.charts}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="penalty" fill="#ff4d4f" />
        </BarChart>
      </div>

      {/* 2. Hiển thị Log mềm chi tiết */}
      <div className="logs-container bg-gray-50 p-4 rounded h-64 overflow-y-auto">
        <h3 className="font-semibold mb-2">Chi tiết vi phạm:</h3>
        {Object.entries(data.logs_soft).map(([rule, info]: [string, any]) => (
          <div key={rule} className="mb-3 border-b pb-2">
            <strong className="text-blue-600">{rule}</strong> - Phạt: <span className="text-red-500">{info.score} điểm</span> <br/>
            <p className="text-sm text-gray-700 mt-1">{info.details}</p>
          </div>
        ))}
      </div>
    </div>
  );
}