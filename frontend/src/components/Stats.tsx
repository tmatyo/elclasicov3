"use client";
import { StatProps, FetchResultStats } from "@/types/app";
import { useEffect, useState } from "react";

const statusQuo = {
	id: 0,
	matches: 0,
	barca: 0,
	draw: 0,
	real: 0,
	barca_goals: 0,
	real_goals: 0,
	avg_attendance: 0,
	created_at: "",
};

export default function Stats(props: StatProps) {
	const [stats, setStats] = useState<FetchResultStats>(statusQuo);

	useEffect(() => {
		if (props.data.length > 0) {
			setStats(props.data[0]);
		}
	}, []);

	return (
		<div className="my-12 flex justify-center flex-col items-center">
			<h2 className="text-center text-3xl font-bold text-heading mb-8">Štatistiky</h2>
			<table>
				<tbody>
					<tr>
						<th className="p-2.5 text-center bg-[#24355a] text-white">Zápasy</th>
						<th className="p-2.5 text-center bg-[#24355a] text-white">Barcelona</th>
						<th className="p-2.5 text-center bg-[#24355a] text-white">Remíza</th>
						<th className="p-2.5 text-center bg-[#24355a] text-white">Real Madrid</th>
						<th className="p-2.5 text-center bg-[#24355a] text-white">Na góly</th>
						<th className="p-2.5 text-center bg-[#24355a] text-white">Priemerná návštevnosť</th>
					</tr>
					<tr>
						<td className="p-2.5 text-center bg-[#24355a] text-white">{stats.matches}</td>
						<td className="p-2.5 text-center bg-[#24355a] text-white">{stats.barca}</td>
						<td className="p-2.5 text-center bg-[#24355a] text-white">{stats.draw}</td>
						<td className="p-2.5 text-center bg-[#24355a] text-white">{stats.real}</td>
						<td className="p-2.5 text-center bg-[#24355a] text-white">{`${stats.barca_goals}:${stats.real_goals}`}</td>
						<td className="p-2.5 text-center bg-[#24355a] text-white">{stats.avg_attendance}</td>
					</tr>
				</tbody>
			</table>
		</div>
	);
}
