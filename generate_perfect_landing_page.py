# -*- coding: utf-8 -*-
"""
RAKSHASETU AI — Full Ultra-Premium Landing Page Generator
Matches media_1793253881309_8d3e40b3.jpg pixel-for-pixel across all 9 sections.
"""

import sys

def generate():
    output_path = "/Users/krishnavarshithkamanaboina/Desktop/Nvidia/rakshasetu/frontend/src/app/page.tsx"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(r"""'use client';

import React, { useState, useEffect, useRef } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import {
  Shield,
  ArrowRight,
  GitFork,
  Cpu,
  Layers,
  CheckCircle2,
  AlertTriangle,
  Play,
  Zap,
  Lock,
  Menu,
  X,
  ChevronRight,
  ChevronDown,
  FileCheck2,
  Search,
  Network,
  Box,
  RefreshCw,
  BarChart3,
  Radar,
  Server,
  Terminal,
  Activity,
  Workflow,
  Clock,
  AlertOctagon,
  Database,
  Key,
  ShieldCheck,
  Eye,
  SlidersHorizontal,
  FileText,
  RotateCcw,
  Sparkles,
  ArrowUpRight,
  Check,
  Code2,
  Gauge,
  Radio,
  Sliders,
  Send,
  Linkedin,
  Twitter,
  Youtube,
  Github,
} from 'lucide-react';
import { useAuth } from '@/lib/auth-context';
import { api } from '@/lib/api';
import CyberCanvas, { CANONICAL_NODES } from '@/components/CyberCanvas';

/* ═══════════════════════════════════════════════════════════════════════
   1. BRAND ASSETS & LOGOS
   ═══════════════════════════════════════════════════════════════════════ */

function RakshasetuShield({ className = 'w-6 h-6' }: { className?: string }) {
  return (
    <svg viewBox="0 0 32 36" fill="none" xmlns="http://www.w3.org/2000/svg" className={className}>
      <path
        d="M16 2L3 6.5V17C3 25 8.5 31.5 16 34C23.5 31.5 29 25 29 17V6.5L16 2Z"
        stroke="#C68E6D"
        strokeWidth="2"
        strokeLinejoin="round"
        fill="#11141B"
      />
      <path d="M10 13V24M22 13V24" stroke="#E8E3DB" strokeWidth="1.5" strokeLinecap="round" />
      <path
        d="M6 18C10 15 14 15 16 17C18 15 22 15 26 18"
        stroke="#C68E6D"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
      <path d="M10 20H22" stroke="#C68E6D" strokeWidth="1.2" strokeLinecap="round" />
      <circle cx="16" cy="11" r="1.5" fill="#D7A384" />
    </svg>
  );
}

function NvidiaLogo({ className = 'w-4 h-4' }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" className={className}>
      <path d="M8.948 6.257c-1.465 0-2.822.42-3.957 1.134a9.712 9.712 0 0 0-4.991 8.544c0 3.791 2.222 7.086 5.467 8.652-.164-.727-.254-1.474-.254-2.228 0-4.045 2.508-7.551 6.183-8.824-1.439-.816-2.448-2.34-2.448-4.095 0-1.745.998-3.26 2.426-4.081-.884-.336-1.848-.521-2.854-.521L8.948 6.257zm7.643 1.092c-2.47 0-4.484 2.015-4.484 4.484 0 2.47 2.014 4.484 4.484 4.484 2.47 0 4.484-2.014 4.484-4.484 0-2.469-2.014-4.484-4.484-4.484zm-7.643 4.484c0 1.258.536 2.404 1.401 3.208-1.579.882-2.651 2.56-2.651 4.488 0 .548.094 1.077.256 1.579C6.01 19.865 4.773 17.65 4.773 15.08c0-3.32 2.083-6.177 5.06-7.34-.564.811-.885 1.785-.885 2.827v.266zm10.74 3.738a9.696 9.696 0 0 0 4.312-8.109c0-5.385-4.366-9.752-9.752-9.752-2.31 0-4.437.808-6.117 2.164 1.157-.735 2.535-1.164 4.01-1.164 3.992 0 7.243 3.25 7.243 7.243 0 2.378-1.15 4.498-2.929 5.834 1.442.81 2.518 2.215 2.873 3.904l.36-.12z" />
    </svg>
  );
}

/* ═══════════════════════════════════════════════════════════════════════
   2. GLOWING SECTION DIVIDER WITH ORBITAL FLARE
   ═══════════════════════════════════════════════════════════════════════ */

function GlowingSectionDivider() {
  return (
    <div className="relative w-full py-4 pointer-events-none overflow-hidden flex items-center justify-center">
      {/* Horizontal laser track */}
      <div className="absolute inset-x-0 h-px bg-gradient-to-r from-transparent via-[#C68E6D]/35 to-transparent" />
      {/* Left flare burst */}
      <div className="absolute -left-12 w-48 h-12 bg-gradient-to-r from-[#C68E6D]/25 to-transparent blur-xl" />
      {/* Right flare burst */}
      <div className="absolute -right-12 w-48 h-12 bg-gradient-to-l from-[#C68E6D]/25 to-transparent blur-xl" />
      {/* Center glowing bead */}
      <div className="w-28 h-0.5 rounded-full bg-gradient-to-r from-transparent via-[#E8E3DB] to-transparent shadow-[0_0_16px_#C68E6D]" />
    </div>
  );
}

/* ═══════════════════════════════════════════════════════════════════════
   3. DATA TYPES & CANONICAL DEFINITIONS
   ═══════════════════════════════════════════════════════════════════════ */

interface FailureMode {
  id: string;
  badge: string;
  title: string;
  sourceNode: string;
  affectedServices: string[];
  disruptionLevel: 'High' | 'Critical' | 'Medium';
  tagColor: string;
  narrative: string;
  rootCause: string;
}

const FAILURE_MODES: FailureMode[] = [
  {
    id: 'policy_drift',
    badge: 'XACML / ABAC Policy Engine',
    title: 'Conditional Access Policy Drift',
    sourceNode: 'Access Policy Engine',
    affectedServices: ['Warehouse System (WMS)', 'Fleet Dispatch Portal'],
    disruptionLevel: 'High',
    tagColor: '#E5AE52',
    narrative: 'A mid-day policy sync drifted rule WS-POLICY-001 from ALLOW to DENY, blocking warehouse operators and fleet dispatchers without human sign-off.',
    rootCause: 'Silent ABAC attribute expression change evaluated during routine automated deployment.',
  },
  {
    id: 'idp_partition',
    badge: 'Federation Gateway',
    title: 'Primary IdP SAML Assertion Partition',
    sourceNode: 'Primary Identity Provider',
    affectedServices: ['Order Management', 'Warehouse System (WMS)', 'Fleet Dispatch Portal'],
    disruptionLevel: 'Critical',
    tagColor: '#E66E73',
    narrative: 'Signing certificate rollover latency partitioned downstream operational applications from root federated claims.',
    rootCause: 'Cryptographic assertion signing key expiration combined with upstream gateway rate limits.',
  },
  {
    id: 'token_flood',
    badge: 'OAuth2 / OIDC Bus',
    title: 'OAuth Token Flood & Queue Starvation',
    sourceNode: 'Order Management',
    affectedServices: ['Order Management'],
    disruptionLevel: 'Medium',
    tagColor: '#36C995',
    narrative: 'Exponential client retry loops following an upstream assertion hiccup caused token endpoint starvation, freezing order processing queues.',
    rootCause: 'Non-idempotent client retry storm flooding OAuth /token authorization server endpoints.',
  },
  {
    id: 'dag_cascade',
    badge: 'Multi-Hop Identity DAG',
    title: 'Non-Linear Dependency Deadlock',
    sourceNode: 'Recovery Controller',
    affectedServices: ['Fleet Dispatch Portal', 'Warehouse System (WMS)'],
    disruptionLevel: 'High',
    tagColor: '#E5AE52',
    narrative: 'An outage in a shared permission group cascaded across middleware scopes and service accounts in an unexpected topological sequence.',
    rootCause: 'Circular attribute dependency between dispatch worker pools and warehouse pick validation rules.',
  },
];

interface WorkflowStage {
  id: string;
  name: string;
  icon: React.ElementType;
  badge: string;
  summary: string;
  col1: { title: string; desc: string };
  col2: { title: string; desc: string };
  col3: { title: string; desc: string };
  col4: { title: string; desc: string };
}

const WORKFLOW_STAGES: WorkflowStage[] = [
  {
    id: '01',
    name: 'DETECT',
    icon: Radar,
    badge: 'Active Monitoring (300s) ● Live',
    summary: 'Identify identity authentication anomalies, policy drift across enterprise directories in real time.',
    col1: { title: '01. INGEST', desc: 'SAML assertions, OAuth/OIDC failures, directory access logs.' },
    col2: { title: '02. ANALYZE', desc: 'Detect anomalies, policy drifts, and access pattern deviations.' },
    col3: { title: '03. CORRELATE', desc: 'Map to affected services and business operations.' },
    col4: { title: '04. CLASSIFY', desc: 'Assign risk level and trigger investigation agents.' },
  },
  {
    id: '02',
    name: 'INVESTIGATE',
    icon: Search,
    badge: 'Nemotron Multi-Hop Agent',
    summary: 'Autonomous root-cause tracing across federated directories, IAM event buses, and policy repositories.',
    col1: { title: '01. PARSE DIFFS', desc: 'Cross-reference Okta/Azure change logs against historical rules.' },
    col2: { title: '02. TRAVERSE DAG', desc: 'Trace graph dependencies to identify anomalous configuration nodes.' },
    col3: { title: '03. ISOLATE ROOT', desc: 'Determine rule WS-POLICY-001 drifted from ALLOW to DENY.' },
    col4: { title: '04. CONFIDENCE', desc: 'Evaluate causal probability (0.98 diagnostic confidence score).' },
  },
  {
    id: '03',
    name: 'REASON',
    icon: Cpu,
    badge: 'NVIDIA Nemotron Super-49B',
    summary: 'Formal reasoning across threat models, compliance rules, and operational business dependencies.',
    col1: { title: '01. CONSTRAINTS', desc: 'Verify zero-trust guardrails and compliance baseline requirements.' },
    col2: { title: '02. WEIGH PATHS', desc: 'Evaluate minimal-change rollback vs hotfix assertion token.' },
    col3: { title: '03. RISK SCORING', desc: 'Calculate disruption index and blast radius for candidate fixes.' },
    col4: { title: '04. SELECT PLAYBOOK', desc: 'Select deterministic atomic rollback with scoped guardrails.' },
  },
  {
    id: '04',
    name: 'PLAN',
    icon: Box,
    badge: 'Digital Twin Sandbox Twin',
    summary: 'Dry-run proposed recovery playbooks in an isolated identity sandbox twin before execution.',
    col1: { title: '01. CLONE TWIN', desc: 'Spin up air-gapped container replica of enterprise directory state.' },
    col2: { title: '02. INJECT PATCH', desc: 'Apply candidate policy patch in isolated simulation environment.' },
    col3: { title: '03. TEST TOKENS', desc: 'Replay synthetic login transactions across downstream services.' },
    col4: { title: '04. PASS PROOF', desc: 'Verify 0% disruption score and 100% simulated access restoration.' },
  },
  {
    id: '05',
    name: 'AUTHORIZE',
    icon: Lock,
    badge: 'Cryptographic Dual-Custody',
    summary: 'Enforce cryptographic human-in-the-loop authorization before any potentially disruptive action.',
    col1: { title: '01. DOSSIER', desc: 'Generate complete Nemotron reasoning trace and verification evidence.' },
    col2: { title: '02. CHALLENGE', desc: 'Require FIDO2 / WebAuthn cryptographic approval challenge.' },
    col3: { title: '03. DUAL-SIGN', desc: 'Collect multi-party senior operator signatures for sensitive actions.' },
    col4: { title: '04. IMMUTABLE LOG', desc: 'Record cryptographic signature on append-only audit ledger.' },
  },
  {
    id: '06',
    name: 'RECOVER',
    icon: RefreshCw,
    badge: 'Deterministic Orchestrator',
    summary: 'Orchestrate deterministic remediation actions across federated identity providers and caches.',
    col1: { title: '01. ATOMIC PATCH', desc: 'Apply targeted policy reversion via verified IdP management APIs.' },
    col2: { title: '02. FLUSH CACHE', desc: 'Purge stale negative authorization decision cache entries.' },
    col3: { title: '03. RESTORE FLOW', desc: 'Re-enable assertion token exchange for isolated services.' },
    col4: { title: '04. TOPOLOGY SYNC', desc: 'Validate all downstream edge nodes transition to operational.' },
  },
  {
    id: '07',
    name: 'VERIFY',
    icon: ShieldCheck,
    badge: 'Dual-Assertion Verification',
    summary: 'Conduct independent cryptographic access verification across multiple trust paths.',
    col1: { title: '01. TEST ASSERTIONS', desc: 'Execute live synthetic logins across all recovered service endpoints.' },
    col2: { title: '02. ZERO-TRUST CHECK', desc: 'Verify no unintended permissions or bypasses were granted.' },
    col3: { title: '03. LATENCY CHECK', desc: 'Measure authentication round-trip latency against baseline SLA.' },
    col4: { title: '04. CLOSE TICKET', desc: 'Issue cryptographic post-incident report and seal audit trail.' },
  },
];

/* ═══════════════════════════════════════════════════════════════════════
   4. ACTIVE BLAST RADIUS TOPOLOGY SVG (PROBLEM SECTION)
   ═══════════════════════════════════════════════════════════════════════ */

function ActiveBlastRadiusTopology({ activeFailureId }: { activeFailureId: string }) {
  const isPolicyDrift = activeFailureId === 'policy_drift';
  const isIdpPartition = activeFailureId === 'idp_partition';
  const isTokenFlood = activeFailureId === 'token_flood';

  return (
    <div className="relative w-full h-[360px] sm:h-[400px] bg-[#0E121A]/95 rounded-2xl border border-white/[0.08] p-4 sm:p-5 flex flex-col justify-between overflow-hidden shadow-2xl">
      {/* Top Header of Diagram */}
      <div className="flex items-center justify-between border-b border-white/[0.06] pb-3 text-xs">
        <div className="flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-[#E5AE52] animate-pulse" />
          <span className="font-mono-tech tracking-wider uppercase font-semibold text-[#E8E3DB]">
            ACTIVE BLAST RADIUS TOPOLOGY
          </span>
        </div>
        <div className="px-2.5 py-1 rounded-md text-[11px] font-mono-tech font-bold bg-[#E66E73]/15 text-[#E66E73] border border-[#E66E73]/30">
          Affected Services: {isTokenFlood ? '1 Isolated' : isIdpPartition ? '3 Isolated' : '2 Isolated'}
        </div>
      </div>

      {/* SVG Connecting Links with Animated Signal Packets */}
      <svg className="absolute inset-0 w-full h-full pointer-events-none z-0">
        <defs>
          <linearGradient id="grad-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#36C995" stopOpacity="0.8" />
            <stop offset="100%" stopColor="#36C995" stopOpacity="0.2" />
          </linearGradient>
          <linearGradient id="grad-amber" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#E5AE52" stopOpacity="0.9" />
            <stop offset="100%" stopColor="#E5AE52" stopOpacity="0.3" />
          </linearGradient>
          <linearGradient id="grad-red" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#E66E73" stopOpacity="0.9" />
            <stop offset="100%" stopColor="#E66E73" stopOpacity="0.3" />
          </linearGradient>
        </defs>

        {/* Link: Primary IdP to Recovery Controller */}
        <line x1="28%" y1="26%" x2="67%" y2="48%" stroke="#36C995" strokeWidth="1.5" strokeOpacity="0.35" />
        
        {/* Link: Access Policy Engine to Recovery Controller */}
        <line
          x1="78%"
          y1="26%"
          x2="67%"
          y2="48%"
          stroke={isPolicyDrift ? '#E5AE52' : '#36C995'}
          strokeWidth={isPolicyDrift ? '2.2' : '1.5'}
          strokeDasharray={isPolicyDrift ? '4 3' : 'none'}
          strokeOpacity="0.75"
        />

        {/* Link: Recovery Controller to Warehouse System */}
        <line
          x1="67%"
          y1="56%"
          x2="24%"
          y2="76%"
          stroke={isPolicyDrift || isIdpPartition ? '#E66E73' : '#36C995'}
          strokeWidth="2"
          strokeDasharray={isPolicyDrift || isIdpPartition ? '5 3' : 'none'}
        />

        {/* Link: Recovery Controller to Fleet Dispatch */}
        <line
          x1="67%"
          y1="56%"
          x2="53%"
          y2="76%"
          stroke={isPolicyDrift || isIdpPartition ? '#E66E73' : '#36C995'}
          strokeWidth="2"
          strokeDasharray={isPolicyDrift || isIdpPartition ? '5 3' : 'none'}
        />

        {/* Link: Recovery Controller to Order Management */}
        <line
          x1="67%"
          y1="56%"
          x2="84%"
          y2="76%"
          stroke={isTokenFlood || isIdpPartition ? '#E66E73' : '#36C995'}
          strokeWidth="2"
          strokeDasharray={isTokenFlood || isIdpPartition ? '5 3' : 'none'}
        />
      </svg>

      {/* Interactive Topology Node Grid */}
      <div className="relative z-10 flex-1 grid grid-cols-12 grid-rows-3 gap-2 sm:gap-3 py-2 items-center">
        {/* TOP ROW: Primary IdP Gateway (Left) & Access Policy Engine (Right) */}
        <div className="col-span-6 sm:col-span-5 self-start">
          <div className="bg-[#141A22]/95 border border-[#36C995]/50 rounded-xl p-2.5 sm:p-3 shadow-lg">
            <div className="flex items-center gap-1.5 text-[10px] font-mono-tech text-[#36C995] font-semibold uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-[#36C995]" />
              <span>OPERATIONAL</span>
            </div>
            <div className="text-xs sm:text-sm font-display font-bold text-white mt-0.5">Primary IdP Gateway</div>
            <div className="text-[10px] font-mono-tech text-[#9DA3AF]">SAML 2.0 / OIDC Fed</div>
          </div>
        </div>

        <div className="col-span-6 sm:col-span-5 sm:col-start-8 self-start">
          <div className={`rounded-xl p-2.5 sm:p-3 shadow-lg transition-all ${
            isPolicyDrift
              ? 'bg-[#141A22]/95 border-2 border-[#E5AE52] shadow-[0_0_24px_rgba(229,174,82,0.35)]'
              : 'bg-[#141A22]/95 border border-white/10'
          }`}>
            <div className="flex items-center gap-1.5 text-[10px] font-mono-tech text-[#E5AE52] font-semibold uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-[#E5AE52] animate-ping" />
              <span>ROOT DRIFT</span>
            </div>
            <div className="text-xs sm:text-sm font-display font-bold text-white mt-0.5">Access Policy Engine</div>
            <div className="text-[10px] font-mono-tech text-[#E5AE52]">Rule WS-POLICY-001</div>
          </div>
        </div>

        {/* CENTER ROW: Recovery Controller (Centered) */}
        <div className="col-span-8 col-start-3 sm:col-span-6 sm:col-start-4 self-center">
          <div className="bg-[#141A22]/95 border border-[#36C995]/50 rounded-xl p-2.5 sm:p-3 shadow-lg text-center">
            <div className="flex items-center justify-center gap-1.5 text-[10px] font-mono-tech text-[#36C995] font-semibold uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-[#36C995]" />
              <span>OPERATIONAL</span>
            </div>
            <div className="text-xs sm:text-sm font-display font-bold text-white mt-0.5">Recovery Controller</div>
            <div className="text-[10px] font-mono-tech text-[#9DA3AF]">Air-Gapped Sandbox Twin</div>
          </div>
        </div>

        {/* BOTTOM ROW: Warehouse System (Left), Fleet Dispatch (Center), Order Management (Right) */}
        <div className="col-span-4 self-end">
          <div className={`rounded-xl p-2 sm:p-2.5 shadow-lg transition-all ${
            isPolicyDrift || isIdpPartition
              ? 'bg-[#141A22]/95 border-2 border-[#E66E73] shadow-[0_0_20px_rgba(230,110,115,0.35)]'
              : 'bg-[#141A22]/95 border border-[#36C995]/50'
          }`}>
            <div className="flex items-center gap-1 text-[9px] font-mono-tech text-[#E66E73] font-semibold uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-[#E66E73] animate-pulse" />
              <span>ISOLATED (403)</span>
            </div>
            <div className="text-[11px] sm:text-xs font-display font-bold text-white mt-0.5 truncate">Warehouse System</div>
            <div className="text-[9px] font-mono-tech text-[#9DA3AF] truncate">125 Logistics Operators</div>
          </div>
        </div>

        <div className="col-span-4 self-end">
          <div className={`rounded-xl p-2 sm:p-2.5 shadow-lg transition-all ${
            isPolicyDrift || isIdpPartition
              ? 'bg-[#141A22]/95 border-2 border-[#E66E73] shadow-[0_0_20px_rgba(230,110,115,0.35)]'
              : 'bg-[#141A22]/95 border border-[#36C995]/50'
          }`}>
            <div className="flex items-center gap-1 text-[9px] font-mono-tech text-[#E66E73] font-semibold uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-[#E66E73] animate-pulse" />
              <span>ISOLATED (403)</span>
            </div>
            <div className="text-[11px] sm:text-xs font-display font-bold text-white mt-0.5 truncate">Fleet Dispatch Portal</div>
            <div className="text-[9px] font-mono-tech text-[#9DA3AF] truncate">580 Fleet Drivers</div>
          </div>
        </div>

        <div className="col-span-4 self-end">
          <div className={`rounded-xl p-2 sm:p-2.5 shadow-lg transition-all ${
            isTokenFlood
              ? 'bg-[#141A22]/95 border-2 border-[#E66E73] shadow-[0_0_20px_rgba(230,110,115,0.35)]'
              : 'bg-[#141A22]/95 border border-[#36C995]/50'
          }`}>
            <div className="flex items-center gap-1 text-[9px] font-mono-tech text-[#36C995] font-semibold uppercase">
              <span className="w-1.5 h-1.5 rounded-full bg-[#36C995]" />
              <span>OPERATIONAL</span>
            </div>
            <div className="text-[11px] sm:text-xs font-display font-bold text-white mt-0.5 truncate">Order Management</div>
            <div className="text-[9px] font-mono-tech text-[#9DA3AF] truncate">450 Queued Orders</div>
          </div>
        </div>
      </div>

      {/* Bottom Footer Bar */}
      <div className="flex items-center justify-between border-t border-white/[0.06] pt-2 text-[10px] font-mono-tech">
        <div className="text-[#E5AE52]">
          SOURCE: <span className="text-white">Access Policy Engine</span>
        </div>
        <div className="text-[#9DA3AF]">NetworkX Graph • Sub-second BFS Traversal</div>
      </div>
    </div>
  );
}

/* ═══════════════════════════════════════════════════════════════════════
   5. MAIN EXPORTED PAGE COMPONENT
   ═══════════════════════════════════════════════════════════════════════ */

export default function LandingPage() {
  const router = useRouter();
  const { demoLogin } = useAuth();

  // State Management
  const [selectedHeroNode, setSelectedHeroNode] = useState<string | null>(null);
  const [activeFailureId, setActiveFailureId] = useState<string>('policy_drift');
  const [activeConsoleTab, setActiveConsoleTab] = useState<string>('incident');
  const [activeWorkflowStage, setActiveWorkflowStage] = useState<string>('01');
  const [activeArchLayer, setActiveArchLayer] = useState<number>(0);
  const [selectedLabScenario, setSelectedLabScenario] = useState<string>('warehouse_access');
  const [isApplyingLab, setIsApplyingLab] = useState<boolean>(false);
  const [labApplied, setLabApplied] = useState<boolean>(false);
  const [videoModalOpen, setVideoModalOpen] = useState<boolean>(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState<boolean>(false);
  const [activeSection, setActiveSection] = useState<string>('hero');
  const [isConnecting, setIsConnecting] = useState<boolean>(false);

  // Authentication Handlers
  const handleInstantConsole = async () => {
    setIsConnecting(true);
    try {
      await demoLogin();
      router.push('/dashboard');
    } catch {
      router.push('/dashboard');
    } finally {
      setIsConnecting(false);
    }
  };

  const handleApplyScenario = async () => {
    setIsApplyingLab(true);
    try {
      await demoLogin();
      await api.triggerScenario('policy_drift');
      setLabApplied(true);
      setTimeout(() => {
        router.push('/dashboard/incidents');
      }, 1200);
    } catch {
      router.push('/dashboard/incidents');
    } finally {
      setIsApplyingLab(false);
    }
  };

  const currentFailure = FAILURE_MODES.find((f) => f.id === activeFailureId) ?? FAILURE_MODES[0];
  const currentStage = WORKFLOW_STAGES.find((s) => s.id === activeWorkflowStage) ?? WORKFLOW_STAGES[0];

  const ARCH_LAYERS = [
    {
      name: 'Enterprise Applications',
      desc: 'Connectors, data models, and operational context.',
      badge: 'Active Integration',
      integrations: [
        'Warehouse Management System',
        'Order Management Portal',
        'Fleet Logistics & Dispatch',
        'Enterprise ERP Gateway',
      ],
      protocols: ['REST >', 'gRPC >', 'SAML 2.0 >', 'OIDC >', 'SCIM >'],
    },
    {
      name: 'Identity & Access Infrastructure',
      desc: 'Root cryptographic federation authorities and directory controllers.',
      badge: 'Core Identity Bus',
      integrations: ['Azure Entra ID Directory', 'Okta Workforce Identity', 'PingFederate Bridge', 'AWS IAM Identity Center'],
      protocols: ['mTLS >', 'SAML 2.0 Assertion >', 'OIDC Bearer >', 'Kerberos V5 >'],
    },
    {
      name: 'Monitoring & Event Ingestion',
      desc: 'Real-time telemetry streams, assertion log parsing, and access event buses.',
      badge: 'Streaming Telemetry',
      integrations: ['Kafka Access Event Bus', 'CloudTrail Ingest Filter', 'Okta System Log Relay', 'Syslog TLS Forwarder'],
      protocols: ['Kafka >', 'gRPC Stream >', 'Webhook Push >', 'Syslog RFC5424 >'],
    },
    {
      name: 'Agentic Investigations & Planning',
      desc: 'Multi-hop diagnostic graphs powered by NVIDIA Nemotron-Super-49B on Nebius AI Studio.',
      badge: 'NVIDIA Nemotron 49B',
      integrations: ['Multi-Hop Reasoning Agent', 'Graph Traversal Engine', 'Policy Diff Validator', 'Constraint Formulator'],
      protocols: ['OpenAI / Nebius API >', 'Tool Calling JSON >', 'Vector Search >'],
    },
    {
      name: 'Policy & Authorization Controls',
      desc: 'Zero-trust ABAC rule engines, conditional access gatekeepers, and permission boundaries.',
      badge: 'ABAC / XACML Engine',
      integrations: ['OPA Rego Policy Engine', 'AWS Verified Permissions', 'XACML Decision Point', 'Permit.io Gateway'],
      protocols: ['OPA Data API >', 'Cedar Policy >', 'XACML 3.0 >'],
    },
    {
      name: 'Recovery Orchestration',
      desc: 'Air-gapped digital twin sandboxes and deterministic playbook execution engines.',
      badge: 'Digital Twin Sandbox',
      integrations: ['Isolated Container Clones', 'Token Replay Test Suite', 'Atomic Patch Executor', 'Blast Radius Monitor'],
      protocols: ['Docker API >', 'Containerd >', 'IdP Admin REST >'],
    },
    {
      name: 'Audit & Compliance Layer',
      desc: 'Append-only cryptographic signature ledger with FIDO2 dual-custody verification.',
      badge: 'Immutable Ledger',
      integrations: ['Append-Only SHA-256 Ledger', 'WebAuthn Signature Gate', 'Dual-Custody Approvals', 'SOC2 / ISO Evidence Store'],
      protocols: ['WebAuthn / FIDO2 >', 'Ed25519 Signatures >', 'Merkle Tree Ingest >'],
    },
  ];

  return (
    <div className="min-h-screen bg-[#090D13] text-[#E8E3DB] selection:bg-[#C68E6D]/25 selection:text-white font-sans antialiased overflow-x-hidden">
      {/* ─── 1. FIXED LUXURY ENTERPRISE HEADER ─── */}
      <header className="sticky top-0 z-50 w-full border-b border-white/[0.08] bg-[#090D13]/90 backdrop-blur-2xl">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-[72px] flex items-center justify-between gap-4">
          {/* Logo & Monogram */}
          <Link href="/" className="flex items-center gap-3 group shrink-0">
            <RakshasetuShield className="w-8 h-8 group-hover:scale-105 transition-transform" />
            <div className="flex flex-col">
              <span className="font-display font-extrabold text-base tracking-wider text-white">
                RAKSHASETU AI
              </span>
              <span className="font-mono-tech text-[10px] text-[#C68E6D] tracking-widest uppercase">
                रक्षासेतु
              </span>
            </div>
          </Link>

          {/* Desktop Navigation Links Pill Container */}
          <nav className="hidden min-[1150px]:flex items-center gap-1 bg-[#141A22]/90 backdrop-blur-xl border border-white/10 rounded-full px-2 py-1.5 text-xs text-[#9DA3AF]">
            <a
              href="#hero"
              className={`px-3.5 py-1.5 rounded-full transition-all ${
                activeSection === 'hero' || activeSection === 'platform' || activeSection === 'telemetry'
                  ? 'text-white bg-white/[0.08] border border-[#C68E6D]/40 font-semibold'
                  : 'hover:text-white'
              }`}
            >
              Platform
            </a>
            <a href="#problem" className="px-3.5 py-1.5 rounded-full hover:text-white transition-all">How It Works</a>
            <a href="#capabilities" className="px-3.5 py-1.5 rounded-full hover:text-white transition-all">Capabilities</a>
            <a href="#architecture" className="px-3.5 py-1.5 rounded-full hover:text-white transition-all">Architecture</a>
            <a href="#security" className="px-3.5 py-1.5 rounded-full hover:text-white transition-all">Security</a>
            <a href="#lab" className="px-3.5 py-1.5 rounded-full hover:text-white transition-all">Resources</a>
            <a href="#impact" className="px-3.5 py-1.5 rounded-full hover:text-white transition-all">About</a>
          </nav>

          {/* Right Action Buttons */}
          <div className="flex items-center gap-2.5 sm:gap-3 shrink-0">
            <Link
              href="/auth/signin"
              className="px-3.5 sm:px-4 py-2 rounded-xl text-xs font-medium text-[#E8E3DB] bg-[#141A22]/80 border border-white/10 hover:border-[#C68E6D]/50 hover:text-white transition-all whitespace-nowrap"
            >
              Sign In
            </Link>
            <button
              onClick={handleInstantConsole}
              disabled={isConnecting}
              className="hidden sm:flex px-4 py-2 rounded-xl text-xs font-bold text-[#090D13] bg-gradient-to-r from-[#C68E6D] via-[#D7A384] to-[#C68E6D] hover:brightness-110 items-center gap-1.5 transition-all shadow-[0_0_20px_rgba(198,142,109,0.28)] cursor-pointer whitespace-nowrap"
            >
              <span>{isConnecting ? 'Connecting...' : 'Launch Console'}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>

            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="min-[1150px]:hidden p-2 rounded-lg text-[#9DA3AF] hover:text-white hover:bg-white/5 transition-colors"
              aria-label="Toggle navigation menu"
            >
              {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation Drawer */}
        {mobileMenuOpen && (
          <div className="min-[1150px]:hidden fixed top-[72px] left-0 right-0 border-b border-white/[0.08] bg-[#090D13]/98 backdrop-blur-2xl px-6 py-6 space-y-5 shadow-2xl z-50">
            <nav className="flex flex-col space-y-3.5 text-sm font-medium text-[#9DA3AF]">
              <a href="#hero" onClick={() => setMobileMenuOpen(false)} className="hover:text-white py-1">Platform</a>
              <a href="#problem" onClick={() => setMobileMenuOpen(false)} className="hover:text-white py-1">How It Works</a>
              <a href="#capabilities" onClick={() => setMobileMenuOpen(false)} className="hover:text-white py-1">Capabilities</a>
              <a href="#workflow" onClick={() => setMobileMenuOpen(false)} className="hover:text-white py-1">Workflow</a>
              <a href="#architecture" onClick={() => setMobileMenuOpen(false)} className="hover:text-white py-1">Architecture</a>
              <a href="#security" onClick={() => setMobileMenuOpen(false)} className="hover:text-white py-1">Security</a>
              <a href="#lab" onClick={() => setMobileMenuOpen(false)} className="hover:text-white py-1">Resources</a>
              <a href="#impact" onClick={() => setMobileMenuOpen(false)} className="hover:text-white py-1">About</a>
            </nav>
            <div className="pt-4 border-t border-white/[0.08] flex flex-col gap-3">
              <button
                onClick={() => {
                  setMobileMenuOpen(false);
                  handleInstantConsole();
                }}
                className="w-full py-2.5 rounded-xl text-xs font-bold text-[#090D13] bg-[#C68E6D] hover:bg-[#D7A384] flex items-center justify-center gap-2 cursor-pointer"
              >
                <Zap className="w-3.5 h-3.5" />
                <span>Launch Console Demo</span>
              </button>
            </div>
          </div>
        )}
      </header>

      {/* ─── 2. CINEMATIC HERO SECTION (40% Content / 60% 3D Cyber Citadel) ─── */}
      <section
        id="hero"
        className="relative w-full border-b border-white/[0.08] bg-[#090D13] overflow-hidden scroll-mt-24 pt-8 sm:pt-12 pb-8 px-4 sm:px-8 lg:px-16"
      >
        {/* Dynamic Background Volumetric Light Layers */}
        <div className="absolute -top-32 right-[8%] w-[620px] h-[620px] rounded-full bg-gradient-to-br from-[#C68E6D]/12 via-[#A36F52]/06 to-transparent blur-[140px] pointer-events-none animate-aurora-1" />
        <div className="absolute top-[22%] left-[-120px] w-[520px] h-[520px] rounded-full bg-gradient-to-tr from-[#36C995]/06 to-transparent blur-[130px] pointer-events-none animate-aurora-2" />
        <div className="absolute bottom-[-100px] right-[28%] w-[420px] h-[420px] rounded-full bg-gradient-to-t from-[#C68E6D]/08 to-transparent blur-[120px] pointer-events-none" />

        {/* Subtle Precision Geometric Grid */}
        <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,255,255,0.015)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,255,255,0.015)_1px,transparent_1px)] bg-[size:44px_44px] pointer-events-none [mask-image:radial-gradient(ellipse_60%_50%_at_50%_50%,#000_70%,transparent_100%)] opacity-70" />

        {/* Full-width Two-Column Grid: Left 40% Content, Right 60% 3D Citadel */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-center">
          {/* LEFT REGION: 40% */}
          <div className="lg:col-span-5 space-y-6 text-left max-w-xl z-10 animate-in fade-in slide-in-from-bottom-4 duration-700">
            {/* Eyebrow */}
            <div className="inline-flex items-center gap-2 text-xs font-mono-tech tracking-[0.2em] uppercase text-[#C68E6D] font-semibold">
              <span className="w-2 h-2 rounded-full bg-[#C68E6D] shrink-0" />
              <span>AUTONOMOUS IDENTITY RESILIENCE</span>
            </div>

            {/* Main Headline */}
            <h1 className="font-display font-extrabold text-3xl sm:text-4xl md:text-5xl lg:text-[2.9rem] xl:text-[3.4rem] leading-[1.08] tracking-tight text-white">
              When Access Fails,<br />
              <span className="text-white">Security </span>
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#E8E3DB] via-[#D7A384] to-[#C68E6D]">
                Prevails.
              </span>
            </h1>

            {/* Supporting Description */}
            <p className="text-sm sm:text-base text-[#9DA3AF] leading-relaxed font-normal">
              RAKSHASETU AI investigates identity failures, evaluates recovery strategies,
              and verifies secure restoration of critical business access through
              agentic automation.
            </p>

            {/* Two Primary Actions */}
            <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 pt-1">
              <button
                onClick={handleInstantConsole}
                disabled={isConnecting}
                className="px-6 py-3.5 rounded-xl text-xs font-bold text-[#090D13] bg-gradient-to-r from-[#C68E6D] via-[#D7A384] to-[#C68E6D] hover:brightness-110 flex items-center justify-center gap-2 shadow-[0_0_24px_rgba(198,142,109,0.3)] hover:shadow-[0_0_36px_rgba(198,142,109,0.55)] hover:-translate-y-0.5 active:translate-y-0 transition-all cursor-pointer whitespace-nowrap"
              >
                <span>{isConnecting ? 'Connecting...' : 'Launch Recovery Console'}</span>
                <ArrowRight className="w-4 h-4" />
              </button>
              <a
                href="#workflow"
                className="px-6 py-3.5 rounded-xl text-xs font-semibold text-[#E8E3DB] bg-[#141A22]/80 backdrop-blur-md border border-white/15 hover:border-[#C68E6D]/70 hover:bg-white/[0.05] hover:text-white hover:-translate-y-0.5 active:translate-y-0 transition-all text-center flex items-center justify-center gap-2 whitespace-nowrap"
              >
                <span>Explore Workflow</span>
              </a>
            </div>

            {/* Simulation Trace Walkthrough */}
            <div className="pt-1">
              <button
                onClick={() => setVideoModalOpen(true)}
                className="inline-flex items-center gap-2.5 text-xs font-medium text-[#9DA3AF] hover:text-[#C68E6D] transition-colors cursor-pointer group"
              >
                <div className="w-7 h-7 rounded-full border border-white/20 bg-white/5 flex items-center justify-center group-hover:border-[#C68E6D] group-hover:bg-[#C68E6D]/10 transition-colors">
                  <Play className="w-3 h-3 text-[#C68E6D] fill-[#C68E6D]" />
                </div>
                <span>See How It Works (Simulation Trace)</span>
              </button>
            </div>

            {/* Technology Attribution */}
            <div className="pt-2 flex flex-wrap items-center gap-3 text-xs text-[#9DA3AF] font-mono-tech border-t border-white/[0.06] pt-4">
              <span>Powered by</span>
              <div className="flex items-center gap-1.5 text-white font-semibold">
                <NvidiaLogo className="w-4 h-4 text-[#76B900]" />
                <span>NVIDIA Nemotron</span>
              </div>
              <span className="text-[#666C78]">×</span>
              <span className="text-[#E8E3DB] font-bold tracking-wider">Nebius AI Studio</span>
            </div>
          </div>

          {/* RIGHT REGION: 60% Seamless Cyber Citadel Viewport */}
          <div className="lg:col-span-7 relative w-full h-[460px] sm:h-[540px] lg:h-[620px] xl:h-[680px] bg-transparent flex items-center justify-center">
            <CyberCanvas
              selectedNodeId={selectedHeroNode}
              onSelectNode={setSelectedHeroNode}
            />
          </div>
        </div>

        {/* ─── Dedicated Telemetry Status Section Directly Beneath Hero ─── */}
        <div id="telemetry" className="mt-8 pt-6 border-t border-white/[0.06] space-y-3">
          <div className="flex items-center justify-between pb-1 text-[11px] font-mono-tech tracking-wider uppercase">
            <div className="flex items-center gap-2 text-[#36C995]">
              <span className="w-1.5 h-1.5 rounded-full bg-[#36C995] animate-pulse" />
              <span className="font-bold text-[#E8E3DB]">SIMULATED ENVIRONMENT TELEMETRY STATUS</span>
            </div>
            <div className="text-[#9DA3AF] text-[10px] hidden sm:block">
              CONTROLLED SANDBOX METRICS • REAL-TIME SYNC
            </div>
          </div>

          <div className="bg-[#141A22]/90 backdrop-blur-xl border border-white/[0.12] rounded-2xl p-3 sm:p-4 grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 shadow-2xl">
            {/* Card 1 */}
            <Link
              href="/dashboard/infrastructure"
              className="flex items-center justify-between p-2.5 rounded-xl hover:bg-white/[0.04] transition-colors cursor-pointer group"
            >
              <div className="flex items-center gap-3">
                <div className="w-9 h-9 rounded-xl bg-[#1B222C] border border-[#C68E6D]/30 flex items-center justify-center shrink-0 group-hover:border-[#C68E6D] transition-colors">
                  <Shield className="w-4 h-4 text-[#C68E6D]" />
                </div>
                <div>
                  <span className="text-xl sm:text-2xl font-display font-extrabold text-white">4</span>
                  <div className="text-[11px] font-mono-tech text-[#9DA3AF] group-hover:text-white transition-colors flex items-center gap-1">
                    <span>Connected Applications</span>
                    <ChevronRight className="w-3 h-3 text-[#C68E6D]" />
                  </div>
                </div>
              </div>
              {/* Sparkline & Trend */}
              <div className="flex items-center gap-2">
                <svg className="w-14 h-5 stroke-[#36C995] fill-none" viewBox="0 0 56 20">
                  <path d="M0 14 Q14 16 28 8 T56 4" strokeWidth="1.8" />
                </svg>
                <span className="text-[11px] font-mono-tech font-bold text-[#36C995]">+2</span>
              </div>
            </Link>

            {/* Card 2 */}
            <Link
              href="/dashboard/recovery"
              className="flex items-center justify-between p-2.5 rounded-xl hover:bg-white/[0.04] transition-colors cursor-pointer group"
            >
              <div className="flex items-center gap-3">
                <div className="w-9 h-9 rounded-xl bg-[#1B222C] border border-[#C68E6D]/30 flex items-center justify-center shrink-0 group-hover:border-[#C68E6D] transition-colors">
                  <Cpu className="w-4 h-4 text-[#C68E6D]" />
                </div>
                <div>
                  <span className="text-xl sm:text-2xl font-display font-extrabold text-white">2</span>
                  <div className="text-[11px] font-mono-tech text-[#9DA3AF] group-hover:text-white transition-colors flex items-center gap-1">
                    <span>Recovery Procedures</span>
                    <ChevronRight className="w-3 h-3 text-[#C68E6D]" />
                  </div>
                </div>
              </div>
              {/* Sparkline & Trend */}
              <div className="flex items-center gap-2">
                <svg className="w-14 h-5 stroke-[#36C995] fill-none" viewBox="0 0 56 20">
                  <path d="M0 10 Q14 10 28 10 T56 10" strokeWidth="1.8" />
                </svg>
                <span className="text-[11px] font-mono-tech font-bold text-[#36C995]">+0</span>
              </div>
            </Link>

            {/* Card 3 */}
            <Link
              href="/dashboard/incidents"
              className="flex items-center justify-between p-2.5 rounded-xl hover:bg-white/[0.04] transition-colors cursor-pointer group"
            >
              <div className="flex items-center gap-3">
                <div className="w-9 h-9 rounded-xl bg-[#E66E73]/15 border border-[#E66E73]/40 flex items-center justify-center shrink-0 group-hover:border-[#E66E73] transition-colors">
                  <AlertTriangle className="w-4 h-4 text-[#E66E73]" />
                </div>
                <div>
                  <span className="text-xl sm:text-2xl font-display font-extrabold text-[#E66E73]">1</span>
                  <div className="text-[11px] font-mono-tech text-[#E66E73] group-hover:text-white transition-colors flex items-center gap-1">
                    <span>Active Simulated Incident</span>
                    <ChevronRight className="w-3 h-3 text-[#E66E73]" />
                  </div>
                </div>
              </div>
              {/* Sparkline & Trend */}
              <div className="flex items-center gap-2">
                <svg className="w-14 h-5 stroke-[#E66E73] fill-none" viewBox="0 0 56 20">
                  <path d="M0 16 Q14 4 28 12 T56 6" strokeWidth="1.8" />
                </svg>
                <span className="text-[11px] font-mono-tech font-bold text-[#E66E73]">-1</span>
              </div>
            </Link>

            {/* Card 4 */}
            <Link
              href="/dashboard/audit"
              className="flex items-center justify-between p-2.5 rounded-xl hover:bg-white/[0.04] transition-colors cursor-pointer group"
            >
              <div className="flex items-center gap-3">
                <div className="w-9 h-9 rounded-xl bg-[#36C995]/15 border border-[#36C995]/40 flex items-center justify-center shrink-0 group-hover:border-[#36C995] transition-colors">
                  <ShieldCheck className="w-4 h-4 text-[#36C995]" />
                </div>
                <div>
                  <span className="text-xl sm:text-2xl font-display font-extrabold text-[#36C995]">4</span>
                  <div className="text-[11px] font-mono-tech text-[#36C995] group-hover:text-white transition-colors flex items-center gap-1">
                    <span>Completed Verification Runs</span>
                    <ChevronRight className="w-3 h-3 text-[#36C995]" />
                  </div>
                </div>
              </div>
              {/* Sparkline & Trend */}
              <div className="flex items-center gap-2">
                <svg className="w-14 h-5 stroke-[#36C995] fill-none" viewBox="0 0 56 20">
                  <path d="M0 14 Q14 16 28 6 T56 2" strokeWidth="1.8" />
                </svg>
                <span className="text-[11px] font-mono-tech font-bold text-[#36C995]">+3</span>
              </div>
            </Link>
          </div>
        </div>
      </section>

      {/* Orbital Divider */}
      <GlowingSectionDivider />

      {/* ─── 3. THE OPERATIONAL PROBLEM (Exact Reference Layout) ─── */}
      <section
        id="problem"
        className="relative w-full border-b border-white/[0.08] bg-[#090D13] scroll-mt-24 py-16 px-4 sm:px-8 lg:px-16 overflow-hidden"
      >
        <div className="max-w-7xl mx-auto space-y-10">
          {/* Section Header */}
          <div className="space-y-3 max-w-3xl">
            <div className="inline-flex items-center gap-2 text-xs font-mono-tech tracking-[0.2em] uppercase text-[#C68E6D] font-semibold">
              <span className="w-2 h-2 rounded-full bg-[#C68E6D]" />
              <span>THE OPERATIONAL PROBLEM</span>
            </div>
            <h2 className="font-display font-extrabold text-2xl sm:text-3xl lg:text-4xl leading-tight text-white">
              When Identity Infrastructure Drifts, Every Downstream Enterprise System Freezes.
            </h2>
            <p className="text-sm sm:text-base text-[#9DA3AF] leading-relaxed">
              Enterprise identity is not an isolated directory — it is a Directed Acyclic Graph (DAG)
              connecting authentication authorities, policy engines, and frontline operational applications.
              A minor misconfiguration cascades instantly.
            </p>
          </div>

          {/* Two-Column Split Layout */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            {/* Left Column: Failure Mode Selector (5 cols) */}
            <div className="lg:col-span-5 space-y-3">
              <div className="text-[11px] font-mono-tech tracking-wider uppercase text-[#9DA3AF] font-bold pb-1">
                SELECT SIMULATED FAILURE MODE:
              </div>

              {FAILURE_MODES.map((mode) => {
                const isActive = activeFailureId === mode.id;

                return (
                  <button
                    key={mode.id}
                    onClick={() => setActiveFailureId(mode.id)}
                    className={`w-full text-left p-4 rounded-xl border transition-all cursor-pointer flex items-center justify-between gap-3 ${
                      isActive
                        ? 'bg-[#141A22] border-2 border-[#E5AE52] shadow-[0_0_24px_rgba(229,174,82,0.22)]'
                        : 'bg-[#141A22]/60 border-white/[0.08] hover:border-white/20 hover:bg-[#141A22]'
                    }`}
                  >
                    <div className="space-y-1">
                      <div className="flex items-center gap-2">
                        <span
                          className={`w-2 h-2 rounded-full ${
                            isActive ? 'bg-[#E5AE52] animate-pulse' : 'bg-[#9DA3AF]'
                          }`}
                        />
                        <span className="text-xs sm:text-sm font-display font-bold text-white">
                          {mode.title}
                        </span>
                      </div>
                      <div className="text-[11px] font-mono-tech text-[#9DA3AF] pl-4">
                        Source: {mode.sourceNode}
                      </div>
                    </div>
                    <div className="flex items-center gap-2 shrink-0">
                      <span
                        className="px-2 py-0.5 rounded text-[10px] font-mono-tech font-bold uppercase"
                        style={{
                          backgroundColor: `${mode.tagColor}15`,
                          color: mode.tagColor,
                          border: `1px solid ${mode.tagColor}40`,
                        }}
                      >
                        {mode.disruptionLevel}
                      </span>
                      <ChevronRight
                        className={`w-4 h-4 transition-transform ${
                          isActive ? 'text-[#E5AE52] translate-x-0.5' : 'text-[#666C78]'
                        }`}
                      />
                    </div>
                  </button>
                );
              })}
            </div>

            {/* Right Column: Active Blast Radius Topology Diagram (7 cols) */}
            <div className="lg:col-span-7">
              <ActiveBlastRadiusTopology activeFailureId={activeFailureId} />
            </div>
          </div>
        </div>
      </section>

      {/* Orbital Divider */}
      <GlowingSectionDivider />

      {/* ─── 4. ENTERPRISE CAPABILITIES SUITE (Exact Reference Layout) ─── */}
      <section
        id="capabilities"
        className="relative w-full border-b border-white/[0.08] bg-[#090D13] scroll-mt-24 py-16 px-4 sm:px-8 lg:px-16 overflow-hidden"
      >
        <div className="max-w-7xl mx-auto space-y-10">
          {/* Section Header */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div className="space-y-3 max-w-3xl">
              <div className="inline-flex items-center gap-2 text-xs font-mono-tech tracking-[0.2em] uppercase text-[#C68E6D] font-semibold">
                <span className="w-2 h-2 rounded-full bg-[#C68E6D]" />
                <span>ENTERPRISE CAPABILITIES SUITE</span>
              </div>
              <h2 className="font-display font-extrabold text-2xl sm:text-3xl lg:text-4xl leading-tight text-white">
                Architectural Resilience for Identity Infrastructure
              </h2>
              <p className="text-sm sm:text-base text-[#9DA3AF] leading-relaxed">
                Autonomous multi-hop investigation, real-time dependency topology, air-gapped simulation twins,
                and deterministic verification gates.
              </p>
            </div>
            <button
              onClick={handleInstantConsole}
              className="px-5 py-2.5 rounded-xl text-xs font-bold text-[#090D13] bg-gradient-to-r from-[#C68E6D] to-[#D7A384] hover:brightness-110 flex items-center gap-2 shrink-0 shadow-lg cursor-pointer whitespace-nowrap self-start md:self-auto"
            >
              <span>Launch Enterprise Console</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* Top Console Tabs Bar */}
          <div className="flex items-center gap-2 overflow-x-auto pb-2 border-b border-white/[0.08] text-xs font-medium text-[#9DA3AF] no-scrollbar">
            {[
              { id: 'incident', label: 'Incident Resolution', icon: FileText },
              { id: 'workflow', label: 'Recovery Workflows', icon: Workflow },
              { id: 'dag', label: 'Dependency Graph', icon: Network },
              { id: 'verify', label: 'Verification Runs', icon: CheckCircle2 },
              { id: 'policy', label: 'Policy Compliance', icon: Shield },
              { id: 'audit', label: 'Audit Logs', icon: FileCheck2 },
              { id: 'security', label: 'Security Controls', icon: Lock },
            ].map((tab) => {
              const Icon = tab.icon;
              const isActive = activeConsoleTab === tab.id;

              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveConsoleTab(tab.id)}
                  className={`px-3.5 py-1.5 rounded-full flex items-center gap-2 transition-all whitespace-nowrap cursor-pointer ${
                    isActive
                      ? 'bg-[#C68E6D] text-[#090D13] font-bold shadow-md'
                      : 'hover:text-white hover:bg-white/[0.05]'
                  }`}
                >
                  <Icon className="w-3.5 h-3.5" />
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </div>

          {/* 3-Tier Asymmetric Capability Box Layout */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            {/* Box 1 (Left 4 cols): Featured Incident Triage */}
            <div className="lg:col-span-5 bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 sm:p-6 flex flex-col justify-between space-y-5 shadow-2xl">
              <div className="space-y-4">
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-lg bg-[#E66E73]/15 border border-[#E66E73]/30 flex items-center justify-center">
                    <AlertTriangle className="w-4 h-4 text-[#E66E73]" />
                  </div>
                  <div>
                    <span className="text-[10px] font-mono-tech uppercase font-bold text-[#E66E73]">
                      INC-2024-0841 • ACTIVE TRIAGE
                    </span>
                    <h3 className="text-base sm:text-lg font-display font-bold text-white">
                      Warehouse Access Denial (Policy Drift WS-POLICY-001)
                    </h3>
                  </div>
                </div>

                {/* 3 Metrics Pills */}
                <div className="grid grid-cols-3 gap-2 py-1">
                  <div className="bg-[#1B222C] rounded-lg p-2 text-center border border-white/[0.05]">
                    <div className="text-xs sm:text-sm font-display font-extrabold text-[#36C995]">1.4s</div>
                    <div className="text-[9px] font-mono-tech text-[#9DA3AF]">Root Cause Identified</div>
                  </div>
                  <div className="bg-[#1B222C] rounded-lg p-2 text-center border border-white/[0.05]">
                    <div className="text-xs sm:text-sm font-display font-extrabold text-[#E5AE52]">WS-POLICY-001</div>
                    <div className="text-[9px] font-mono-tech text-[#9DA3AF]">Affected Rule</div>
                  </div>
                  <div className="bg-[#1B222C] rounded-lg p-2 text-center border border-white/[0.05]">
                    <div className="text-xs sm:text-sm font-display font-extrabold text-[#E66E73]">High</div>
                    <div className="text-[9px] font-mono-tech text-[#9DA3AF]">Impact Level</div>
                  </div>
                </div>

                <p className="text-xs sm:text-sm text-[#9DA3AF] leading-relaxed">
                  Autonomous agents analyze the full identity graph, identify configuration drift,
                  and generate safe, minimal recovery actions with verification.
                </p>
              </div>

              <Link
                href="/dashboard/incidents"
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-bold text-[#090D13] bg-[#C68E6D] hover:bg-[#D7A384] transition-all cursor-pointer w-fit"
              >
                <span>Inspect in Console</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </Link>
            </div>

            {/* Box 2 (Center 3.5 cols): DAG Blast Radius Mapping */}
            <div className="lg:col-span-3 bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 flex flex-col justify-between space-y-4 shadow-2xl">
              <div>
                <div className="flex items-center gap-2 text-[10px] font-mono-tech uppercase font-bold text-[#C68E6D]">
                  <Network className="w-3.5 h-3.5" />
                  <span>DAG BLAST RADIUS MAPPING</span>
                </div>

                {/* Circular Hub Visualization */}
                <div className="relative w-full aspect-square max-h-[190px] mx-auto my-2 flex items-center justify-center">
                  <div className="absolute inset-0 rounded-full border border-dashed border-white/10" />
                  <div className="w-14 h-14 rounded-full bg-[#1B222C] border-2 border-[#C68E6D] flex items-center justify-center text-center p-1 shadow-lg z-10">
                    <span className="text-[8px] font-mono-tech font-bold text-white leading-tight">
                      Recovery Controller
                    </span>
                  </div>
                  {/* Surrounding Nodes */}
                  <div className="absolute top-2 left-6 w-7 h-7 rounded-full bg-[#36C995]/20 border border-[#36C995] flex items-center justify-center text-[9px] text-[#36C995] font-bold">W</div>
                  <div className="absolute top-2 right-6 w-7 h-7 rounded-full bg-[#E5AE52]/20 border border-[#E5AE52] flex items-center justify-center text-[9px] text-[#E5AE52] font-bold">P</div>
                  <div className="absolute bottom-2 left-6 w-7 h-7 rounded-full bg-[#E66E73]/20 border border-[#E66E73] flex items-center justify-center text-[9px] text-[#E66E73] font-bold">F</div>
                  <div className="absolute bottom-2 right-6 w-7 h-7 rounded-full bg-[#36C995]/20 border border-[#36C995] flex items-center justify-center text-[9px] text-[#36C995] font-bold">O</div>
                </div>

                {/* Legend List */}
                <div className="space-y-1.5 text-[11px] font-mono-tech">
                  <div className="flex items-center justify-between text-[#9DA3AF]">
                    <span>● 6 Identity Nodes</span>
                    <span className="text-white font-semibold">Healthy</span>
                  </div>
                  <div className="flex items-center justify-between text-[#9DA3AF]">
                    <span>● 12 Policy Dependencies</span>
                    <span className="text-white font-semibold">Active</span>
                  </div>
                  <div className="flex items-center justify-between text-[#E66E73]">
                    <span>● 2 Isolated Services</span>
                    <span className="font-bold">403 Denied</span>
                  </div>
                  <div className="flex items-center justify-between text-[#36C995]">
                    <span>● 4 Recovery Paths</span>
                    <span className="font-bold">Simulated</span>
                  </div>
                </div>
              </div>

              <Link
                href="/dashboard/infrastructure"
                className="text-[11px] font-mono-tech text-[#C68E6D] hover:underline flex items-center gap-1 pt-2 border-t border-white/[0.06]"
              >
                <span>View Full Topology</span>
                <ChevronRight className="w-3 h-3" />
              </Link>
            </div>

            {/* Box 3 (Right 3.5 cols): Digital Twin Pre-Commit Validation */}
            <div className="lg:col-span-4 bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 flex flex-col justify-between space-y-4 shadow-2xl">
              <div>
                <div className="flex items-center gap-2 text-[10px] font-mono-tech uppercase font-bold text-[#36C995]">
                  <Box className="w-3.5 h-3.5" />
                  <span>DIGITAL TWIN PRE-COMMIT VALIDATION</span>
                </div>

                {/* 3D Chip Illustration Graphic */}
                <div className="relative w-full h-32 my-2 flex items-center justify-center overflow-hidden rounded-xl bg-[#090D13]/60 border border-white/[0.05]">
                  <img
                    src="/images/digital-twin-chip-clean.png"
                    alt="Digital Twin 3D Sandbox Processor"
                    className="max-h-full max-w-full object-contain filter drop-shadow-[0_0_16px_rgba(198,142,109,0.3)]"
                  />
                </div>

                {/* 4 Checkpoint Items */}
                <div className="space-y-2 text-xs">
                  <div className="flex items-center gap-2 text-[#E8E3DB]">
                    <CheckCircle2 className="w-4 h-4 text-[#36C995] shrink-0" />
                    <span>Simulate Recovery Actions</span>
                  </div>
                  <div className="flex items-center gap-2 text-[#E8E3DB]">
                    <CheckCircle2 className="w-4 h-4 text-[#36C995] shrink-0" />
                    <span>Validate Policy Compliance</span>
                  </div>
                  <div className="flex items-center gap-2 text-[#E8E3DB]">
                    <CheckCircle2 className="w-4 h-4 text-[#36C995] shrink-0" />
                    <span>Check Downstream Impact</span>
                  </div>
                  <div className="flex items-center gap-2 text-[#E8E3DB]">
                    <CheckCircle2 className="w-4 h-4 text-[#36C995] shrink-0" />
                    <span>Generate Approval Report</span>
                  </div>
                </div>
              </div>

              <button
                onClick={handleInstantConsole}
                className="text-[11px] font-mono-tech text-[#36C995] hover:underline flex items-center gap-1 pt-2 border-t border-white/[0.06] cursor-pointer"
              >
                <span>Run Simulation</span>
                <ChevronRight className="w-3 h-3" />
              </button>
            </div>
          </div>

          {/* Bottom 4 Compact Technical Rows */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-2">
            <div className="bg-[#141A22]/80 rounded-xl border border-white/[0.08] p-4 space-y-2">
              <div className="w-8 h-8 rounded-lg bg-[#C68E6D]/15 border border-[#C68E6D]/30 flex items-center justify-center text-[#C68E6D]">
                <Radio className="w-4 h-4" />
              </div>
              <h4 className="text-xs font-display font-bold text-white">Streaming Telemetry Ingestion</h4>
              <p className="text-[11px] text-[#9DA3AF] leading-relaxed">
                Real-time identity events, audit logs, and system telemetry across directories.
              </p>
            </div>

            <div className="bg-[#141A22]/80 rounded-xl border border-white/[0.08] p-4 space-y-2">
              <div className="w-8 h-8 rounded-lg bg-[#C68E6D]/15 border border-[#C68E6D]/30 flex items-center justify-center text-[#C68E6D]">
                <Key className="w-4 h-4" />
              </div>
              <h4 className="text-xs font-display font-bold text-white">Cryptographic Dual-Custody</h4>
              <p className="text-[11px] text-[#9DA3AF] leading-relaxed">
                Multi-party approval with FIDO2 hardware attestation for sensitive recovery actions.
              </p>
            </div>

            <div className="bg-[#141A22]/80 rounded-xl border border-white/[0.08] p-4 space-y-2">
              <div className="w-8 h-8 rounded-lg bg-[#C68E6D]/15 border border-[#C68E6D]/30 flex items-center justify-center text-[#C68E6D]">
                <Lock className="w-4 h-4" />
              </div>
              <h4 className="text-xs font-display font-bold text-white">Non-Linear Reasoning</h4>
              <p className="text-[11px] text-[#9DA3AF] leading-relaxed">
                Agentic multi-hop analysis across complex Directed Acyclic Graphs (DAG).
              </p>
            </div>

            <div className="bg-[#141A22]/80 rounded-xl border border-white/[0.08] p-4 space-y-2">
              <div className="w-8 h-8 rounded-lg bg-[#C68E6D]/15 border border-[#C68E6D]/30 flex items-center justify-center text-[#C68E6D]">
                <ShieldCheck className="w-4 h-4" />
              </div>
              <h4 className="text-xs font-display font-bold text-white">Deterministic Verification</h4>
              <p className="text-[11px] text-[#9DA3AF] leading-relaxed">
                Replay and validate recovery in air-gapped sandbox digital twin environments.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Orbital Divider */}
      <GlowingSectionDivider />

      {/* ─── 5. INTERACTIVE SEVEN-STAGE RECOVERY PROGRESSION (WORKFLOW) ─── */}
      <section
        id="workflow"
        className="relative w-full border-b border-white/[0.08] bg-[#090D13] scroll-mt-24 py-16 px-4 sm:px-8 lg:px-16 overflow-hidden"
      >
        <div className="max-w-7xl mx-auto space-y-10">
          {/* Section Header */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div className="space-y-3 max-w-3xl">
              <div className="inline-flex items-center gap-2 text-xs font-mono-tech tracking-[0.2em] uppercase text-[#C68E6D] font-semibold">
                <span className="w-2 h-2 rounded-full bg-[#C68E6D]" />
                <span>SEVEN-STAGE AGENTIC LIFECYCLE</span>
              </div>
              <h2 className="font-display font-extrabold text-2xl sm:text-3xl lg:text-4xl leading-tight text-white">
                Interactive Seven-Stage Recovery Progression
              </h2>
              <p className="text-sm sm:text-base text-[#9DA3AF] leading-relaxed">
                Step through the seven-stage autonomous resilience lifecycle during a simulated federated identity outage.
              </p>
            </div>
            <div className="flex items-center gap-3">
              <button
                onClick={() => setVideoModalOpen(true)}
                className="px-4 py-2.5 rounded-xl text-xs font-medium text-[#E8E3DB] bg-[#141A22] border border-white/10 hover:border-white/20 transition-all cursor-pointer"
              >
                View Execution Trace
              </button>
              <button
                onClick={handleInstantConsole}
                className="px-4 py-2.5 rounded-xl text-xs font-bold text-[#090D13] bg-[#C68E6D] hover:bg-[#D7A384] transition-all cursor-pointer"
              >
                Launch in Console
              </button>
            </div>
          </div>

          {/* 7-Stage Horizontal Stepper with Illuminated Line */}
          <div className="relative w-full py-6">
            <div className="absolute top-1/2 left-6 right-6 -translate-y-1/2 h-0.5 bg-white/10 pointer-events-none" />
            <div className="relative z-10 flex items-center justify-between">
              {WORKFLOW_STAGES.map((stg) => {
                const Icon = stg.icon;
                const isActive = activeWorkflowStage === stg.id;

                return (
                  <button
                    key={stg.id}
                    onClick={() => setActiveWorkflowStage(stg.id)}
                    className="flex flex-col items-center gap-2 group cursor-pointer"
                  >
                    <div
                      className={`w-11 h-11 sm:w-13 sm:h-13 rounded-full flex items-center justify-center transition-all ${
                        isActive
                          ? 'bg-[#141A22] border-2 border-[#C68E6D] shadow-[0_0_24px_rgba(198,142,109,0.8)] scale-110'
                          : 'bg-[#141A22] border border-white/20 hover:border-white/40 group-hover:scale-105'
                      }`}
                    >
                      <Icon className={`w-5 h-5 ${isActive ? 'text-[#C68E6D]' : 'text-[#9DA3AF]'}`} />
                    </div>
                    <span
                      className={`text-[10px] sm:text-xs font-mono-tech tracking-wider uppercase font-bold ${
                        isActive ? 'text-white' : 'text-[#9DA3AF]'
                      }`}
                    >
                      {stg.name}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Unified 4-Column Active Stage Deep Inspection Card */}
          <div className="bg-[#141A22] rounded-2xl border border-white/[0.12] p-5 sm:p-6 shadow-2xl space-y-5">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-white/[0.08] pb-4">
              <div className="space-y-1">
                <span className="text-[10px] font-mono-tech uppercase font-bold text-[#C68E6D]">
                  ACTIVE STAGE INSPECTION
                </span>
                <h3 className="text-sm sm:text-base font-display font-bold text-white">
                  {currentStage.name} — {currentStage.summary}
                </h3>
              </div>
              <div className="px-3 py-1 rounded-full text-xs font-mono-tech font-bold bg-[#36C995]/15 text-[#36C995] border border-[#36C995]/30 shrink-0 w-fit">
                {currentStage.badge}
              </div>
            </div>

            {/* 4 Pillars Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="bg-[#1B222C] rounded-xl p-4 border border-white/[0.05] space-y-1.5">
                <div className="text-xs font-mono-tech font-bold text-[#C68E6D]">{currentStage.col1.title}</div>
                <div className="text-xs text-[#9DA3AF] leading-relaxed">{currentStage.col1.desc}</div>
              </div>
              <div className="bg-[#1B222C] rounded-xl p-4 border border-white/[0.05] space-y-1.5">
                <div className="text-xs font-mono-tech font-bold text-[#C68E6D]">{currentStage.col2.title}</div>
                <div className="text-xs text-[#9DA3AF] leading-relaxed">{currentStage.col2.desc}</div>
              </div>
              <div className="bg-[#1B222C] rounded-xl p-4 border border-white/[0.05] space-y-1.5">
                <div className="text-xs font-mono-tech font-bold text-[#C68E6D]">{currentStage.col3.title}</div>
                <div className="text-xs text-[#9DA3AF] leading-relaxed">{currentStage.col3.desc}</div>
              </div>
              <div className="bg-[#1B222C] rounded-xl p-4 border border-white/[0.05] space-y-1.5">
                <div className="text-xs font-mono-tech font-bold text-[#C68E6D]">{currentStage.col4.title}</div>
                <div className="text-xs text-[#9DA3AF] leading-relaxed">{currentStage.col4.desc}</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Orbital Divider */}
      <GlowingSectionDivider />

      {/* ─── 6. SEVEN-LAYER ENTERPRISE RESILIENCE ARCHITECTURE ─── */}
      <section
        id="architecture"
        className="relative w-full border-b border-white/[0.08] bg-[#090D13] scroll-mt-24 py-16 px-4 sm:px-8 lg:px-16 overflow-hidden"
      >
        <div className="max-w-7xl mx-auto space-y-10">
          {/* Eyebrow & Title */}
          <div className="space-y-3 max-w-3xl">
            <div className="inline-flex items-center gap-2 text-xs font-mono-tech tracking-[0.2em] uppercase text-[#C68E6D] font-semibold">
              <span className="w-2 h-2 rounded-full bg-[#C68E6D]" />
              <span>SEVEN-LAYER ENTERPRISE RESILIENCE ARCHITECTURE</span>
            </div>
            <h2 className="font-display font-extrabold text-2xl sm:text-3xl lg:text-4xl leading-tight text-white">
              Layered Cryptographic Infrastructure
            </h2>
          </div>

          {/* 3-Column Interactive Architecture Explorer */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            {/* Left Column (4 cols): 7 Layer Selector Buttons */}
            <div className="lg:col-span-4 space-y-2">
              {ARCH_LAYERS.map((layer, idx) => {
                const isActive = activeArchLayer === idx;

                return (
                  <button
                    key={layer.name}
                    onClick={() => setActiveArchLayer(idx)}
                    className={`w-full text-left p-3 rounded-xl border transition-all cursor-pointer flex items-center justify-between ${
                      isActive
                        ? 'bg-[#141A22] border-2 border-[#C68E6D] shadow-[0_0_20px_rgba(198,142,109,0.3)] text-white'
                        : 'bg-[#141A22]/50 border-white/[0.08] hover:border-white/20 text-[#9DA3AF]'
                    }`}
                  >
                    <div className="flex items-center gap-2.5">
                      <span className="text-[11px] font-mono-tech text-[#C68E6D] font-bold">0{idx + 1}</span>
                      <span className="text-xs font-display font-semibold text-white">{layer.name}</span>
                    </div>
                    <ChevronRight className={`w-3.5 h-3.5 ${isActive ? 'text-[#C68E6D]' : 'text-[#666C78]'}`} />
                  </button>
                );
              })}
            </div>

            {/* Center Column (4.5 cols): Active Layer Detail */}
            <div className="lg:col-span-4 bg-[#141A22] rounded-2xl border border-white/[0.12] p-5 sm:p-6 shadow-2xl space-y-4">
              <div className="flex items-center justify-between border-b border-white/[0.08] pb-3">
                <div>
                  <h3 className="text-base font-display font-bold text-white">
                    {ARCH_LAYERS[activeArchLayer].name}
                  </h3>
                  <p className="text-xs text-[#9DA3AF]">{ARCH_LAYERS[activeArchLayer].desc}</p>
                </div>
                <span className="px-2.5 py-0.5 rounded text-[10px] font-mono-tech font-bold bg-[#36C995]/15 text-[#36C995] border border-[#36C995]/30 shrink-0">
                  {ARCH_LAYERS[activeArchLayer].badge}
                </span>
              </div>

              {/* Core Integrations */}
              <div className="space-y-2">
                <span className="text-[10px] font-mono-tech uppercase font-bold text-[#C68E6D]">
                  CORE INTEGRATIONS
                </span>
                <div className="grid grid-cols-2 gap-2">
                  {ARCH_LAYERS[activeArchLayer].integrations.map((item) => (
                    <div key={item} className="bg-[#1B222C] rounded-lg p-2 text-[11px] text-[#E8E3DB] border border-white/[0.05] truncate">
                      {item}
                    </div>
                  ))}
                </div>
              </div>

              {/* Data Protocols */}
              <div className="space-y-2 pt-2 border-t border-white/[0.06]">
                <span className="text-[10px] font-mono-tech uppercase font-bold text-[#C68E6D]">
                  DATA PROTOCOLS
                </span>
                <div className="flex flex-wrap gap-1.5">
                  {ARCH_LAYERS[activeArchLayer].protocols.map((proto) => (
                    <span key={proto} className="px-2 py-0.5 rounded text-[10px] font-mono-tech bg-white/[0.05] text-[#9DA3AF] border border-white/10">
                      {proto}
                    </span>
                  ))}
                </div>
              </div>
            </div>

            {/* Right Column (3.5 cols): 3D Layer Stack Illustration */}
            <div className="lg:col-span-4 bg-[#141A22] rounded-2xl border border-white/[0.12] p-4 flex items-center justify-center overflow-hidden shadow-2xl h-[340px]">
              <img
                src="/images/arch-layer-stack-clean.png"
                alt="7-Layer Architecture 3D Stack"
                className="max-h-full max-w-full object-contain filter drop-shadow-[0_0_20px_rgba(198,142,109,0.35)]"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Orbital Divider */}
      <GlowingSectionDivider />

      {/* ─── 7. SECURITY ARCHITECTURE PRINCIPLES ─── */}
      <section
        id="security"
        className="relative w-full border-b border-white/[0.08] bg-[#090D13] scroll-mt-24 py-16 px-4 sm:px-8 lg:px-16 overflow-hidden"
      >
        <div className="max-w-7xl mx-auto space-y-10">
          {/* Eyebrow & Headline */}
          <div className="space-y-3 max-w-3xl">
            <div className="inline-flex items-center gap-2 text-xs font-mono-tech tracking-[0.2em] uppercase text-[#C68E6D] font-semibold">
              <span className="w-2 h-2 rounded-full bg-[#C68E6D]" />
              <span>SECURITY ARCHITECTURE PRINCIPLES</span>
            </div>
            <h2 className="font-display font-extrabold text-2xl sm:text-3xl lg:text-4xl leading-tight text-white">
              Autonomous Intelligence. Controlled Execution.
            </h2>
            <p className="text-sm sm:text-base text-[#9DA3AF] leading-relaxed">
              Engineered around four foundational zero-trust principles, cryptographic safety guards,
              and deterministic execution guarantees.
            </p>
          </div>

          {/* 4 Horizontal Security Panels */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            <div className="bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-3 shadow-xl hover:border-[#C68E6D]/50 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-[#C68E6D]/15 border border-[#C68E6D]/30 flex items-center justify-center text-[#C68E6D]">
                <Lock className="w-5 h-5" />
              </div>
              <h3 className="text-sm font-display font-bold text-white">
                Least-Privilege Permissive Boundaries
              </h3>
              <p className="text-xs text-[#9DA3AF] leading-relaxed">
                Temporary, scoped access with just-enough elevation. Automatic revocation after recovery completion.
              </p>
            </div>

            <div className="bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-3 shadow-xl hover:border-[#C68E6D]/50 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-[#C68E6D]/15 border border-[#C68E6D]/30 flex items-center justify-center text-[#C68E6D]">
                <Key className="w-5 h-5" />
              </div>
              <h3 className="text-sm font-display font-bold text-white">
                Cryptographic Dual-Custody Approval
              </h3>
              <p className="text-xs text-[#9DA3AF] leading-relaxed">
                Destructive actions require multi-party approval with cryptographic hardware attestation.
              </p>
            </div>

            <div className="bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-3 shadow-xl hover:border-[#C68E6D]/50 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-[#C68E6D]/15 border border-[#C68E6D]/30 flex items-center justify-center text-[#C68E6D]">
                <Box className="w-5 h-5" />
              </div>
              <h3 className="text-sm font-display font-bold text-white">
                Air-Gapped Digital Twin Simulation
              </h3>
              <p className="text-xs text-[#9DA3AF] leading-relaxed">
                Validate every recovery action in isolated, deterministic sandbox container environments.
              </p>
            </div>

            <div className="bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-3 shadow-xl hover:border-[#C68E6D]/50 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-[#C68E6D]/15 border border-[#C68E6D]/30 flex items-center justify-center text-[#C68E6D]">
                <ShieldCheck className="w-5 h-5" />
              </div>
              <h3 className="text-sm font-display font-bold text-white">
                Dual-Assertion Independent Verification
              </h3>
              <p className="text-xs text-[#9DA3AF] leading-relaxed">
                Independent verification of all identity assertions across multiple independent trust paths.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Orbital Divider */}
      <GlowingSectionDivider />

      {/* ─── 8. INTERACTIVE RECOVERY LABORATORY ─── */}
      <section
        id="lab"
        className="relative w-full border-b border-white/[0.08] bg-[#090D13] scroll-mt-24 py-16 px-4 sm:px-8 lg:px-16 overflow-hidden"
      >
        <div className="max-w-7xl mx-auto space-y-10">
          {/* Header */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div className="space-y-3 max-w-3xl">
              <div className="inline-flex items-center gap-2 text-xs font-mono-tech tracking-[0.2em] uppercase text-[#C68E6D] font-semibold">
                <span className="w-2 h-2 rounded-full bg-[#C68E6D]" />
                <span>INTERACTIVE RECOVERY LABORATORY</span>
              </div>
              <h2 className="font-display font-extrabold text-2xl sm:text-3xl lg:text-4xl leading-tight text-white">
                Simulate Incident Triage in Real Time
              </h2>
              <p className="text-sm sm:text-base text-[#9DA3AF] leading-relaxed">
                Trigger controlled test outages in the safe sandbox environment to observe autonomous root-cause isolation and dual-custody verification.
              </p>
            </div>
            <button
              onClick={handleInstantConsole}
              className="px-5 py-2.5 rounded-xl text-xs font-bold text-[#090D13] bg-gradient-to-r from-[#C68E6D] to-[#D7A384] hover:brightness-110 flex items-center gap-2 shrink-0 shadow-lg cursor-pointer whitespace-nowrap self-start md:self-auto"
            >
              <span>Launch Full Command Console</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* 3-Region Layout */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
            {/* Region 1 (3.5 cols): Select Failure Scenario */}
            <div className="lg:col-span-4 bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-4 shadow-2xl flex flex-col justify-between">
              <div className="space-y-3">
                <div className="text-[10px] font-mono-tech uppercase font-bold text-[#9DA3AF]">
                  1. SELECT FAILURE SCENARIO
                </div>
                <div className="space-y-2">
                  <div className="w-full bg-[#1B222C] border border-white/10 rounded-xl p-3 flex items-center justify-between text-xs text-white">
                    <div className="flex items-center gap-2">
                      <span className="w-2 h-2 rounded-full bg-[#E66E73] animate-pulse" />
                      <span>Warehouse Access Denial (Policy Drift)</span>
                    </div>
                    <ChevronDown className="w-4 h-4 text-[#9DA3AF]" />
                  </div>
                </div>
                <p className="text-xs text-[#9DA3AF] leading-relaxed">
                  Triggers an automated drift injection simulating mid-day ABAC policy divergence across logistics endpoints.
                </p>
              </div>

              <button
                onClick={handleApplyScenario}
                disabled={isApplyingLab || labApplied}
                className="w-full py-3 rounded-xl text-xs font-bold text-[#090D13] bg-[#C68E6D] hover:bg-[#D7A384] transition-all flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50"
              >
                {isApplyingLab ? (
                  <span>Applying Scenario...</span>
                ) : labApplied ? (
                  <span>Applied! Redirecting...</span>
                ) : (
                  <span>Apply Scenario</span>
                )}
              </button>
            </div>

            {/* Region 2 (4 cols): Digital Twin Sandbox */}
            <div className="lg:col-span-4 bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-4 shadow-2xl flex flex-col justify-between">
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-mono-tech uppercase font-bold text-[#36C995]">
                    2. DIGITAL TWIN SANDBOX
                  </span>
                  <span className="px-2 py-0.5 rounded text-[10px] font-mono-tech font-bold bg-[#36C995]/15 text-[#36C995] border border-[#36C995]/30">
                    Environment Ready
                  </span>
                </div>
                {/* 4 Sandbox Nodes */}
                <div className="grid grid-cols-2 gap-2.5">
                  <div className="bg-[#1B222C] rounded-xl p-3 border border-white/[0.05] space-y-1">
                    <Server className="w-4 h-4 text-[#C68E6D]" />
                    <div className="text-[11px] font-display font-bold text-white">Simulated Directory</div>
                    <div className="text-[9px] font-mono-tech text-[#36C995]">Online (Isolated)</div>
                  </div>
                  <div className="bg-[#1B222C] rounded-xl p-3 border border-white/[0.05] space-y-1">
                    <Sliders className="w-4 h-4 text-[#C68E6D]" />
                    <div className="text-[11px] font-display font-bold text-white">Policy Engine</div>
                    <div className="text-[9px] font-mono-tech text-[#E5AE52]">Drift Monitored</div>
                  </div>
                  <div className="bg-[#1B222C] rounded-xl p-3 border border-white/[0.05] space-y-1">
                    <Network className="w-4 h-4 text-[#C68E6D]" />
                    <div className="text-[11px] font-display font-bold text-white">3 Connected Services</div>
                    <div className="text-[9px] font-mono-tech text-[#36C995]">Replay Ready</div>
                  </div>
                  <div className="bg-[#1B222C] rounded-xl p-3 border border-white/[0.05] space-y-1">
                    <Shield className="w-4 h-4 text-[#C68E6D]" />
                    <div className="text-[11px] font-display font-bold text-white">Isolated Network</div>
                    <div className="text-[9px] font-mono-tech text-[#36C995]">Air-Gapped</div>
                  </div>
                </div>
              </div>
              <div className="text-[11px] font-mono-tech text-[#9DA3AF]">
                Zero production impact guaranteed via deterministic container namespaces.
              </div>
            </div>

            {/* Region 3 (4 cols): Verification Trace Terminal */}
            <div className="lg:col-span-4 bg-[#0E121A] rounded-2xl border border-white/[0.08] p-4 font-mono-tech text-[11px] space-y-3 shadow-2xl flex flex-col justify-between">
              <div className="space-y-2">
                <div className="flex items-center justify-between border-b border-white/[0.08] pb-2 text-[#9DA3AF]">
                  <span>3. VERIFICATION TRACE</span>
                  <span className="w-2 h-2 rounded-full bg-[#36C995] animate-ping" />
                </div>
                <div className="space-y-1.5 text-[#9DA3AF]">
                  <p className="text-[#9DA3AF]">[14:22:01] Detecting policy drift in WS-POLICY-001...</p>
                  <p className="text-[#36C995]">[14:22:03] Mapping downstream dependencies...</p>
                  <p className="text-[#E5AE52]">[14:22:05] Generating recovery plan (minimal change)...</p>
                  <p className="text-[#9DA3AF]">[14:22:07] Validating in digital twin environment...</p>
                  <p className="text-[#36C995] font-bold">[14:22:09] Ready for dual-custody approval.</p>
                </div>
              </div>
              <div className="pt-2 border-t border-white/[0.06] text-[10px] text-[#666C78]">
                Session ID: RS-SIM-7819 • Deterministic Seed 0xFA4B
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Orbital Divider */}
      <GlowingSectionDivider />

      {/* ─── 9. EVIDENCE-DRIVEN OPERATIONAL RESILIENCE (IMPACT) ─── */}
      <section
        id="impact"
        className="relative w-full border-b border-white/[0.08] bg-[#090D13] scroll-mt-24 py-16 px-4 sm:px-8 lg:px-16 overflow-hidden"
      >
        <div className="max-w-7xl mx-auto space-y-10">
          {/* Eyebrow & Headline */}
          <div className="space-y-3 max-w-3xl">
            <div className="inline-flex items-center gap-2 text-xs font-mono-tech tracking-[0.2em] uppercase text-[#C68E6D] font-semibold">
              <span className="w-2 h-2 rounded-full bg-[#C68E6D]" />
              <span>EVIDENCE-DRIVEN OPERATIONAL VALUE</span>
            </div>
            <h2 className="font-display font-extrabold text-2xl sm:text-3xl lg:text-4xl leading-tight text-white">
              Evidence-Driven Operational Resilience
            </h2>
            <p className="text-sm sm:text-base text-[#9DA3AF] leading-relaxed">
              Measurable operational improvements across triage duration, blast radius accuracy,
              remediation risk, and regulatory audit-readiness.
            </p>
          </div>

          {/* 4 Comparative Cards with Progress Bars */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            {/* Card 1 */}
            <div className="bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-3 shadow-xl">
              <div className="text-[11px] font-mono-tech text-[#9DA3AF] uppercase">
                Investigation Velocity (MTTR)
              </div>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-display font-extrabold text-white">1.4s</span>
                <span className="text-xs font-mono-tech text-[#9DA3AF] line-through">6.4h</span>
              </div>
              <div className="w-full bg-[#1B222C] rounded-full h-1.5 overflow-hidden">
                <div className="bg-[#36C995] h-full rounded-full w-[99%]" />
              </div>
              <div className="text-[11px] font-mono-tech text-[#36C995] font-bold">
                +99.9% improvement
              </div>
            </div>

            {/* Card 2 */}
            <div className="bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-3 shadow-xl">
              <div className="text-[11px] font-mono-tech text-[#9DA3AF] uppercase">
                Blast Radius Accuracy
              </div>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-display font-extrabold text-white">99.2%</span>
                <span className="text-xs font-mono-tech text-[#9DA3AF] line-through">62%</span>
              </div>
              <div className="w-full bg-[#1B222C] rounded-full h-1.5 overflow-hidden">
                <div className="bg-[#36C995] h-full rounded-full w-[99%]" />
              </div>
              <div className="text-[11px] font-mono-tech text-[#36C995] font-bold">
                +37.2% improvement
              </div>
            </div>

            {/* Card 3 */}
            <div className="bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-3 shadow-xl">
              <div className="text-[11px] font-mono-tech text-[#9DA3AF] uppercase">
                Remediation Disruption Risk
              </div>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-display font-extrabold text-[#36C995]">Low</span>
                <span className="text-xs font-mono-tech text-[#9DA3AF] line-through">High</span>
              </div>
              <div className="w-full bg-[#1B222C] rounded-full h-1.5 overflow-hidden">
                <div className="bg-[#36C995] h-full rounded-full w-[87%]" />
              </div>
              <div className="text-[11px] font-mono-tech text-[#36C995] font-bold">
                -87% risk reduction
              </div>
            </div>

            {/* Card 4 */}
            <div className="bg-[#141A22] rounded-2xl border border-white/[0.08] p-5 space-y-3 shadow-xl">
              <div className="text-[11px] font-mono-tech text-[#9DA3AF] uppercase">
                Audit Provenance & Compliance
              </div>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl font-display font-extrabold text-white">99.6%</span>
                <span className="text-xs font-mono-tech text-[#9DA3AF] line-through">61%</span>
              </div>
              <div className="w-full bg-[#1B222C] rounded-full h-1.5 overflow-hidden">
                <div className="bg-[#36C995] h-full rounded-full w-[99%]" />
              </div>
              <div className="text-[11px] font-mono-tech text-[#36C995] font-bold">
                +38.6% improvement
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ─── 10. LUXURY ENTERPRISE FOOTER (Exact Reference Match) ─── */}
      <footer className="relative w-full border-t border-white/[0.08] bg-[#070A0F] py-14 px-4 sm:px-8 lg:px-16 overflow-hidden">
        <div className="max-w-7xl mx-auto space-y-12">
          {/* Main Footer Row */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 items-start">
            {/* Col 1: Brand & Monogram (4 cols) */}
            <div className="lg:col-span-4 space-y-4">
              <Link href="/" className="flex items-center gap-3">
                <RakshasetuShield className="w-8 h-8" />
                <div className="flex flex-col">
                  <span className="font-display font-extrabold text-base tracking-wider text-white">
                    RAKSHASETU AI
                  </span>
                  <span className="font-mono-tech text-[10px] text-[#C68E6D] tracking-widest uppercase">
                    रक्षासेतु
                  </span>
                </div>
              </Link>
              <p className="text-xs text-[#9DA3AF] max-w-sm leading-relaxed">
                Autonomous identity resilience for mission-critical enterprise directories.
              </p>
              <div className="text-[11px] font-mono-tech text-[#666C78]">
                © 2026 RAKSHASETU AI. All rights reserved.
              </div>
            </div>

            {/* Col 2: Platform Links (2 cols) */}
            <div className="lg:col-span-2 space-y-3">
              <div className="text-xs font-display font-bold text-white tracking-wider">Platform</div>
              <ul className="space-y-2 text-xs text-[#9DA3AF]">
                <li><a href="#workflow" className="hover:text-white transition-colors">How It Works</a></li>
                <li><a href="#capabilities" className="hover:text-white transition-colors">Capabilities</a></li>
                <li><a href="#architecture" className="hover:text-white transition-colors">Architecture</a></li>
              </ul>
            </div>

            {/* Col 3: Resources Links (2 cols) */}
            <div className="lg:col-span-2 space-y-3">
              <div className="text-xs font-display font-bold text-white tracking-wider">Resources</div>
              <ul className="space-y-2 text-xs text-[#9DA3AF]">
                <li><a href="#security" className="hover:text-white transition-colors">Documentation</a></li>
                <li><a href="#problem" className="hover:text-white transition-colors">Case Studies</a></li>
                <li><a href="#lab" className="hover:text-white transition-colors">Research</a></li>
              </ul>
            </div>

            {/* Col 4: Company Links (2 cols) */}
            <div className="lg:col-span-2 space-y-3">
              <div className="text-xs font-display font-bold text-white tracking-wider">Company</div>
              <ul className="space-y-2 text-xs text-[#9DA3AF]">
                <li><a href="#hero" className="hover:text-white transition-colors">About</a></li>
                <li><a href="#hero" className="hover:text-white transition-colors">Careers</a></li>
                <li><a href="#hero" className="hover:text-white transition-colors">News</a></li>
                <li><a href="#hero" className="hover:text-white transition-colors">Contact</a></li>
              </ul>
            </div>

            {/* Col 5: Newsletter & Social (2 cols) */}
            <div className="lg:col-span-2 space-y-3">
              <div className="text-xs font-display font-bold text-white tracking-wider">Subscribe to updates</div>
              <div className="flex items-center gap-1.5 bg-[#141A22] border border-white/10 rounded-xl p-1">
                <input
                  type="email"
                  placeholder="Enter your email"
                  className="bg-transparent px-2.5 py-1 text-xs text-white placeholder-[#666C78] focus:outline-none w-full"
                />
                <button
                  onClick={() => alert('Subscribed to RAKSHASETU AI technical briefs.')}
                  className="p-1.5 rounded-lg bg-[#C68E6D] text-[#090D13] hover:bg-[#D7A384] transition-colors cursor-pointer shrink-0"
                >
                  <Send className="w-3 h-3" />
                </button>
              </div>
              <div className="flex items-center gap-3 pt-1 text-[#9DA3AF]">
                <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="hover:text-white transition-colors">
                  <Linkedin className="w-4 h-4" />
                </a>
                <a href="https://x.com" target="_blank" rel="noreferrer" className="hover:text-white transition-colors">
                  <Twitter className="w-4 h-4" />
                </a>
                <a href="https://youtube.com" target="_blank" rel="noreferrer" className="hover:text-white transition-colors">
                  <Youtube className="w-4 h-4" />
                </a>
                <a href="https://github.com" target="_blank" rel="noreferrer" className="hover:text-white transition-colors">
                  <Github className="w-4 h-4" />
                </a>
              </div>
            </div>
          </div>

          {/* Bottom Attribution Bar */}
          <div className="pt-6 border-t border-white/[0.06] flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] font-mono-tech text-[#666C78]">
            <div className="flex items-center gap-2">
              <span>Built with NVIDIA Nemotron</span>
              <span>•</span>
              <span>Inspired By Design</span>
              <span>•</span>
              <span>Enterprise Ready</span>
            </div>
            <div className="text-[#9DA3AF]">
              RAKSHASETU AI — When Access Fails, Security Prevails.
            </div>
          </div>
        </div>
      </footer>

      {/* ─── 11. WALKTHROUGH SIMULATION MODAL ─── */}
      {videoModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-xl">
          <div className="relative w-full max-w-3xl bg-[#141A22] border border-white/20 rounded-2xl overflow-hidden shadow-2xl">
            <div className="flex items-center justify-between p-4 border-b border-white/10">
              <div className="flex items-center gap-2">
                <Play className="w-4 h-4 text-[#C68E6D]" />
                <span className="text-xs font-mono-tech font-bold text-white uppercase tracking-wider">
                  SIMULATION TRACE WALKTHROUGH
                </span>
              </div>
              <button
                onClick={() => setVideoModalOpen(false)}
                className="p-1 rounded-lg text-[#9DA3AF] hover:text-white hover:bg-white/10 transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="p-6 space-y-4 font-mono-tech text-xs">
              <div className="p-4 rounded-xl bg-[#090D13] border border-white/10 space-y-2">
                <p className="text-[#36C995] font-bold">[14:22:00] INGEST: Polling 6 enterprise nodes...</p>
                <p className="text-[#E5AE52]">[14:22:01] ANOMALY DETECTED: 403 spikes on Warehouse System & Fleet Dispatch.</p>
                <p className="text-white">[14:22:02] INVOKING: NVIDIA Nemotron-Super-49B on Nebius AI Studio...</p>
                <p className="text-[#36C995]">[14:22:04] ROOT CAUSE ISOLATED: Policy WS-POLICY-001 drifted to DENY.</p>
                <p className="text-[#C68E6D]">[14:22:06] DIGITAL TWIN PRE-CHECK: Rollback tested in sandbox twin. Collateral risk: 0%.</p>
                <p className="text-[#36C995]">[14:22:08] DUAL-CUSTODY ATTESTATION: Approved by SecOps with FIDO2 WebAuthn.</p>
                <p className="text-[#36C995] font-bold">[14:22:10] RESTORATION COMPLETE: 125 users and 580 drivers verified operational.</p>
              </div>
              <div className="flex justify-end pt-2">
                <button
                  onClick={() => {
                    setVideoModalOpen(false);
                    handleInstantConsole();
                  }}
                  className="px-4 py-2 rounded-xl text-xs font-bold text-[#090D13] bg-[#C68E6D] hover:bg-[#D7A384] transition-colors cursor-pointer"
                >
                  Open Recovery Console
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
""")
    print("Landing page generated successfully!")

if __name__ == "__main__":
    generate()

