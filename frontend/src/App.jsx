export default function App() {
  return (
    <div className="flex h-screen">
      <aside className="w-60 bg-gray-800 text-white p-4">
        <h1 className="text-xl font-bold mb-4">Меню</h1>
        <ul className="space-y-2">
          <li>Проекты</li>
          <li>Визуализация</li>
          <li>Расчёты</li>
          <li>История</li>
        </ul>
      </aside>
      <main className="flex-1 bg-gray-100 p-6">
        <h2 className="text-2xl font-semibold mb-4">3D Viewer (заглушка)</h2>
        <div className="bg-white border border-gray-300 h-full rounded p-4">[здесь будет 3D]</div>
      </main>
      <aside className="w-64 bg-gray-50 p-4 border-l">
        <h2 className="text-xl font-bold mb-4">Параметры</h2>
        <label className="block mb-2">Глубина</label>
        <input className="w-full border rounded px-2 py-1 mb-4" placeholder="1000 м" />
        <label className="block mb-2">Угол</label>
        <input className="w-full border rounded px-2 py-1 mb-4" placeholder="15°" />
      </aside>
    </div>
  )
}
